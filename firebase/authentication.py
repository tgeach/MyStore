import logging

import firebase_admin
from firebase_admin import auth, credentials
from decouple import config
from django.contrib.auth.models import User
from rest_framework import authentication
from .exceptions import FirebaseError, InvalidAuthToken, MustRefreshAuthToken, NoAuthToken

PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\n" + config("FIREBASE_PRIVATE_KEY") + "\n-----END PRIVATE KEY-----\n"

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": config("FIREBASE_PROJECT_ID"),
        "private_key_id": config("FIREBASE_KEY_ID"),
        "private_key": PRIVATE_KEY.replace("\\n", "\n"),
        "client_email": config("FIREBASE_CLIENT_EMAIL"),
        "client_id": config("FIREBASE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": config("FIREBASE_CLIENT_CERT_URL"),
    }
)
DEFAULT_ADMINS = ["asim@foodmesh.ca", "teddie@foodmesh.ca"]

default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        token = auth_header.split(" ").pop()
        # Todo: Update $mesh-fb with whatever it needs to be 
        if token and token.startswith("$mesh-fb"):
            id_token = token.split("$mesh-fb:").pop
            decoded_token = None
            try:
                decoded_token = auth.verify_id_token(id_token)
            except Exception:
                raise InvalidAuthToken("Invalid auth token")

            if not id_token or not decoded_token:
                return None

            try:
                uid = decoded_token.get("uid")
                staff = decoded_token.get("staff")
                client = decoded_token.get("client")
                email = decoded_token.get("email")

                # did we give this user default permissions yet, internal staff need this set
                if staff is None and client is None:

                    # for internal staff accounts update @foodmesh.ca with whatever email ending you're using

                    if email.endswith("@foodmesh.ca"):
                        logging.error("Adding as staff: " + email)
                        auth.set_custom_user_claims(uid, {"admin": email in DEFAULT_ADMINS, "staff": True})
                    else:
                        logging.error("Adding as client: " + email)
                        auth.set_custom_user_claims(uid, {"client": True})

                    raise MustRefreshAuthToken()

            except Exception as e:
                raise e

            user, created = User.objects.get_or_create(username=uid)

            return user, decoded_token

        return None

from rest_framework import status
from rest_framework.exceptions import APIException


class NoAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "No authentication token provided"
    default_code = "no_auth_token"


class InvalidAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid authentication token provided"
    default_code = "invalid_token"

class MustRefreshAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Token refresh is required"
    default_code = "refresh_id_token"
    refresh_id_token = True

class FirebaseError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "The user provided with the auth token is no a valid Firebase user, it has not Firebase UID"
    default_code = "no_firebase_uid"
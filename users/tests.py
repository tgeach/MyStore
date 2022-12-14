from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        # this line retreives the test database
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'Test_1', 'Teddie', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.user_name, 'Test_1')
        self.assertEqual(super_user.first_name, 'Teddie')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "Test_1")

        with self.assertRaises(ValueError):
            # This test should cause an error since is_superuser=False
            db.objects.create_superuser(
                email='testuser@super.com', user_name='Test_1', first_name='Teddie', password='password', is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='Test_1', first_name='Teddie', password='password', is_staff=False
            )
    
    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com' , 'username1', 'Teddie', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.user_name, 'username1')
        self.assertEqual(user.first_name, 'Teddie')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
             db.objects.create_user(
                email='', user_name='username1', first_name='Teddie', password='password')



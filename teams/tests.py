from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth import get_user_model


class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Teams',
            email='proba@mail.ru',
            password='test123')
        self.assertEqual(user.username, 'Teams')
        self.assertEqual(user.email, 'proba@mail.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@mail.ru',
            password='123_test'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@mail.ru')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)

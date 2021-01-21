from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import CustomUser
class HomePageTests(SimpleTestCase):
    #Test response status code
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    #Test url name and template
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    #Test response status code
    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup')
        self.assertEqual(response.status_code, 200)

    #Test url name and template
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = CustomUser.objects.create_user(
            self.username, 
            self.email, 
            self.school_name)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
    








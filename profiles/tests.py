from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Profile

class ProfileTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'TestUser',
            email = 'test@testmail.com',
            password = 'testpassword'
        )

        self.profile = Profile.objects.create(
            name = 'Test Name',
            age = 30,
            gender = 'Male',
            partner_preferences = 'Female',
            city = "Test City",
            state = "Arizona",
            zodiac = "Aries",
            hobbies_interests = "Testing hobbies",
            description = "Test description"
        )

    def test_string_representation(self):
        profile = Profile(name="Another Name")
        self.assertEqual(str(profile), profile.name)

    def test_profile_content(self):
        self.assertEqual(f'{self.profile.name}', 'Test Name')
        self.assertEqual(f'{self.profile.age}', '30')
        self.assertEqual(f'{self.profile.gender}', 'Male')
        self.assertEqual(f'{self.profile.partner_preferences}', 'Female')
        self.assertEqual(f'{self.profile.city}', 'Test City')
        self.assertEqual(f'{self.profile.state}', 'Arizona')
        self.assertEqual(f'{self.profile.zodiac}', 'Aries')
        self.assertEqual(f'{self.profile.hobbies_interests}', 'Testing hobbies')
        self.assertEqual(f'{self.profile.description}', 'Test description')

    # def test_profile_list_view(self):
    #     response = self.client.get(reverse('profile_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Testing hobbies')

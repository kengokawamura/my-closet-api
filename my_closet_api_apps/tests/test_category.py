from django.test import TestCase
import requests

from my_closet_api_apps.views import create_category
from my_closet_api_apps.models import category
# Create your tests here.

class CreateCategoryTests(TestCase):
    def test_create_category(self):

        # arrange
        expected = 'test category'
        requests.body = {'category_name': 'test category'}
        # act
        create_category(requests)
        # assert
        self.assertEquals(category.name, expected)

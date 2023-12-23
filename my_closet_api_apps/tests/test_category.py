from django.test import TestCase, Client

from my_closet_api_apps.models import Category
# Create your tests here.

class CreateCategoryTests(TestCase):
    def test_create_category(self):

        # arrange
        expected = 'test category'
        body = {"category_name": "test category"}
        client = Client()
        # act
        client.put("/category", data=body, content_type='application/json')
        qs = Category.objects.values()
        # assert
        category = qs[0]
        self.assertEquals(category['name'], expected)

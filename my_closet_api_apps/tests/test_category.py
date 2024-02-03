from django.test import TestCase, Client
import json
from my_closet_api_apps.models import Category
# Create your tests here.

class CreateCategoryTests(TestCase):
    def create_category(self, name):
        return Category.objects.create(name=name)

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
    
    def test_get_category(self):

        # arrange
        expected = 'test category'
        self.create_category(expected)

        client = Client()
        # act
        res = client.get("/category", content_type='application/json')
        res_body = json.loads(res.content.decode('utf-8'))
        # assert
        self.assertEquals(res.status_code, 200)
        self.assertEquals(res_body['categories'][0]['name'], expected)

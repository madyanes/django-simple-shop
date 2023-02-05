from django.test import TestCase
from django.urls import reverse

class CatalogPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('catalog:product_list'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('catalog:product_list'))
        self.assertTemplateUsed(response, 'catalog/product_list.html')

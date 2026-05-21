from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        for i in range(12):
            Recipe.objects.create(title=f"Recipe {i}", category=self.category, description="Test")

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recipes']), 10)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['category'], self.category)
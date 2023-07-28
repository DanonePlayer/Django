from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeURLsTests(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/recipes/')       # noqa: W292
        
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={"category_id": 1})
        self.assertEqual(url, '/recipes/category/1/')       # noqa: W292
        
    def test_recipe_receitas_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={"id": 1})
        self.assertEqual(url, '/recipes/receitas/1/')       # noqa: W292

class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
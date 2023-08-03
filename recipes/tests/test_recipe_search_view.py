from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeSearchViewTest(TestCase):
    def test_recipe_search_uses_correct_view_function(self):
        url = reverse("recipes:search")
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_load_correct_template(self):
        response = self.client.get(reverse("recipes:search") + "?q=teste")
        self.assertTemplateUsed(response, "recipes/pages/search.html")
        
    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse("recipes:search") # + "?q=teste"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse("recipes:search") + "?q=<Teste>"
        response = self.client.get(url)
        self.assertIn(
            "Search for &#x27;&lt;Teste&gt;&#x27;",
            response.content.decode("utf-8")
        )
    
    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = "This is recipe One"
        title2 = "This is recipe Two"

        recipe1 = self.make_recipe(
            slug="one",
            title=title1,
            author_data={"username":"one"}
        )        
        recipe2 = self.make_recipe(
            slug="two",
            title=title2,
            author_data={"username":"two"}
        )

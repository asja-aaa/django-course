from django.test import TestCase
from django.urls import resolve
# Create your tests here.
from list.views import home_page
from  django.http import  HttpRequest
from django.template.loader import render_to_string

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)


# class HomePageTest(TestCase):
#     def test_root_url_resolve_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)
#
#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.content.decode('utf-8')
#         self.assertTrue(html.startswith('<html>'))
#         self.assertIn('<title>To-Do list</title>',html)
#         self.assertTrue(html.endswith('</html>'))


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response,'home.html')


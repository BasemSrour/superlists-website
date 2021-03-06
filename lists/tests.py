from django.test import TestCase


class HomePageTest(TestCase):

	def test_root_url_resoves_to_home_page_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_home_page_returns_correct__html(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))

		self.assertTemplateUsed(response, 'home.html')

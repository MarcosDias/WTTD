# coding: utf-8
from django.test import TestCase

class HomepageTeste(TestCase):
	def setUp(self):
		self.resp = self.client.get('/')

	def test_get(self):
		"""Get / deve retornar o codigo de status 200"""
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""A Homepage deve usar o index.html"""
		self.assertTemplateUsed(self.resp, 'index.html')
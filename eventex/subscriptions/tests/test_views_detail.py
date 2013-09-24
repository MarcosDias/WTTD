# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Marcos Dias', cpf='12345678901',
										email='marcos@dias.com', phone='27-12345678')
		self.resp = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		"""GET /inscricao/(\d)/ deve returnar status 200"""
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""Usar template"""
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

	def test_context(self):
		"""Contexto deve ter uma instância de subscription"""
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		"""Checa se o dado de subscription foi renderizado"""
		self.assertContains(self.resp, 'Marcos Dias')

class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get('/inscricao/0/')
		self.assertEqual(404, response.status_code)
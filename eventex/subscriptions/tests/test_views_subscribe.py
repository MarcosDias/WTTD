# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get(r('subscriptions:subscribe'))

	def test_get(self):
		"""Get /inscricao/ deve retornar o codigo 200"""
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		"""Resposta deve ser de um template renderizado"""
		self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_form.html')

	def test_html(self):
		"""Html deve conter controles de entrada"""
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 4)
		self.assertContains(self.resp, 'type="submit"')

	def test_csrf(self):
		"""Html devem conter símbolo csrf"""
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		"""Contexto deve ter o formulário de inscrição"""
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
	def setUp(self):
		data = dict(name='Marcos Dias', cpf='12345678901',
					email='marcos@dias.com', phone='27-12345678')
		self.resp = self.client.post(r('subscriptions:subscribe'), data)

	def test_post(self):
		"""POST valido deve redirecionar para /inscricao/1/"""
		self.assertEqual(302, self.resp.status_code)

	def test_save(self):
		"""POST valido deve ser salvo"""
		self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
	def setUp(self):
		data = dict(name='Marcos Dias', cpf='000000000000000000000012',
					email='marcos@dias.com', phone='27-12345678')
		self.resp = self.client.post(r('subscriptions:subscribe'), data)

	def test_post(self):
		"""POST invalido nao deve redirecionar"""
		self.assertEqual(200, self.resp.status_code)

	def test_form_errors(self):
		"""Form deve conter erros"""
		self.assertTrue(self.resp.context['form'].errors)

	def test_dont_save(self):
		"""Nao pode ter salvo"""
		self.assertFalse(Subscription.objects.exists())
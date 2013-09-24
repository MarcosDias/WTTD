# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTeste(TestCase):
	def test_form_has_fields(self):
		"""Formulário deve ter 4 campos"""
		form = SubscriptionForm()
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
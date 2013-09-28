# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTeste(TestCase):
	def test_form_has_fields(self):
		"""Formulário deve ter 4 campos"""
		form = SubscriptionForm()
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

	def test_cpf_is_digit(self):
		"""CPF deve haver apenas digitos"""
		form = self.make_validated_form(cpf='ABC123ABC01')
		self.assertItemsEqual(['cpf'], form.errors)

	def test_cpf_has_11_digits(self):
		"""CPF deve haver 11 digitos"""
		form = self.make_validated_form(cpf='1234')
		self.assertItemsEqual(['cpf'], form.errors)

	def test_email_is_optional(self):
		"""Email deve ser opcional"""
		form = self.make_validated_form(email='')
		self.assertFalse(form.errors)

	def test_name_must_be_capitalized(self):
		"""Nome deve ser capitalizado"""
		form = self.make_validated_form(name='MARCOS dias')
		self.assertEqual('Marcos Dias', form.cleaned_data['name'])

	def test_must_inform_email_or_phone(self):
		"""Email ou teleone é opcional, mas
		um deles deve ser informado"""
		form = self.make_validated_form(email='', phone_0='', phone_1='')
		self.assertItemsEqual(['__all__'], form.errors)

	def make_validated_form(self, **kwargs):
		data= dict(name='Marcos Dias', email='marcos@dias.com',
				cpf='12345678901', phone_0='27', phone_1='12334566')
		data.update(kwargs)
		form = SubscriptionForm(data)
		form.is_valid()
		return form
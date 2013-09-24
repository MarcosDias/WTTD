# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Marcos Dias',
			cpf='12345678909',
			email='marcos@dias.com',
			phone='27-12345678'
		)

	def test_create(self):
		"""Subscription deve ter nome, cpf, email e tel"""
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_create_at(self):
		"""Assinatura deve ter created_at automático"""
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Marcos Dias', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
	"""Testes de colunas unicas"""
	def setUp(self):
		#Criar uma primeira entrada para forçar a colisão
		Subscription.objects.create(name='Marcos Dias', cpf='12345678901',
		email='marcos@dias.com', phone='27-12345678')

	def test_cpf_unique(self):
		"""CPF deve ser unico"""
		s = Subscription(name='Marcos Dias', cpf='12345678901', 
						email = 'outro@email.com', phone='27-12345678')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		"""Email deve ser unico"""
		s = Subscription(name='Marcos Dias', cpf='00000000011', 
						email ='marcos@dias.com', phone='27-12345678')
		self.assertRaises(IntegrityError, s.save)

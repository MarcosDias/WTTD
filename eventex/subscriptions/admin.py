# coding: utf-8
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, ugettext as _
from django.contrib import admin
from eventex.subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribe_today', 'paid')
	date_hierarchy = 'created_at'
	search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
	list_filter = ['created_at']

	def subscribe_today(self, obj):
		return obj.created_at.date() == datetime.today().date()

	subscribe_today.short_description = _(u'Inscrito Hoje?')
	subscribe_today.boolean = True

	actions = ['mark_as_paid']
	def mark_as_paid(self, request, queryset):
		count = queryset.update(paid=True)

		msg = ungettext(
			u'%d inscrição foi marcada como paga',
			u'%d inscrições foram marcadas como pagas',
			count
			)
		self.message_user(request, msg % count)

	mark_as_paid.short_description = _('Marcar como pago')

admin.site.register(Subscription, SubscriptionAdmin)
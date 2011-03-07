__author__ = 'Jussi'
from Parking.models import Area, Type, Slot, Queue, Transaction
from django.contrib import admin

class SlotAdmin(admin.ModelAdmin):
	list_display = ('parking_area', 'parking_type', 'note', 'id', 'is_free')

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('slot_name', 'community_name', 'user_name', 'start_date', 'end_date', 'paid', 'is_current')
	list_filter = ('parking_queue__community__city', 'end_date', 'paid',)

	fieldsets = [
		#('Slot information',				{'fields': ['slot_name', 'community_name']}),
		#('User information', 				{'fields': ['slot_name',]}),
		('Date information',				{'fields': ['end_date', ]}),  #start_date
		('Additional information',			{'fields': ['note_transaction', 'paid']}),
		]
class AreaAdmin (admin.ModelAdmin):
	list_display = ('community', 'name', 'need_rental_agreement')

class TypeAdmin (admin.ModelAdmin):
	list_display = ('name','note', 'price_per_month')

class QueueAdmin (admin.ModelAdmin):
	list_display = ('community', 'user', 'register_date', 'note_queue')


admin.site.register(Area, AreaAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Queue, QueueAdmin)
admin.site.register(Transaction, TransactionAdmin)


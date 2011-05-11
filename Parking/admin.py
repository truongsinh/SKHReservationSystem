__author__ = 'Jussi'
from Parking.models import Area, Type, Slot, Queue, Transaction
from django.contrib import admin

class SlotAdmin(admin.ModelAdmin):
	list_display = ('parking_area', 'parking_type', 'note', 'id', 'is_free', 'free')
	list_filter = ('parking_area__community__city','parking_area__community__postal_code', 'parking_type')
	search_fields = ('parking_area__community__city', 'parking_area__community__address', 'parking_area__community__postal_code')
	fieldsets = [
			('Slot information',	{'fields': ['name','parking_area','parking_type',]}),
			('Additional information', 				{'fields': ['note',]}),
				]
class TransactionAdmin(admin.ModelAdmin):
	list_display = ('slot_name', 'community_name', 'user_name', 'start_date', 'end_date', 'paid', 'is_current')
	list_filter = ('parking_queue__community__city', 'end_date', 'paid',)

	fieldsets = [
		('Slot information',				{'fields': ['parking_slot',]}),
		('Queue information', 				{'fields': ['parking_queue',]}),
		('Date information',				{'fields': ['end_date', ]}),  #start_date
		('Additional information',			{'fields': ['note', 'paid']}),
		]
	#readonly_fields = ('start_date',)
class AreaAdmin (admin.ModelAdmin):
	list_display = ('community', 'name', 'need_rental_agreement')
	list_filter = ( 'community__city', 'community__postal_code')
	search_fields = ('community__city', 'community__address', 'community__postal_code', 'name')
	fieldsets = [
			('Area information',	{'fields': ['name','community',]}),
			('Additional information', 				{'fields': ['need_rental_agreement', 'user_in_charge', 'note']}),
				]

class TypeAdmin (admin.ModelAdmin):
	list_display = ('name','note', 'price_per_month')
	list_filter = ('name', 'price_per_month')

class QueueAdmin (admin.ModelAdmin):
	list_display = ('community', 'user', 'register_date', 'note')
	list_filter = ( 'community__city', 'community__postal_code')
	search_fields = ('community__city', 'community__address', 'community__postal_code', 'user__last_name', 'user__first_name')
	fieldsets = [
			('Queue information',	{'fields': ['user','community',]}),
			('Additional information', 				{'fields': ['decision_date','note',]}),
				]

admin.site.register(Area, AreaAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Queue, QueueAdmin)
admin.site.register(Transaction,
					TransactionAdmin
					)


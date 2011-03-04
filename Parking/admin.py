__author__ = 'Jussi'
from Parking.models import Area, Type, Slot, Queue, Transaction
from django.contrib import admin

class SlotAdmin(admin.ModelAdmin):
	list_display = ('parking_area', 'parking_type', 'note', 'id', 'is_free')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]
class TransactionAdmin(admin.ModelAdmin):
	#list_display = ('parking_queue__community', 'user', 'parking_slot', 'start_date', 'paid', 'is_history')

	list_display = ('parking_slot', 'start_date', 'paid', 'is_history', 'is_current')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]
class AreaAdmin (admin.ModelAdmin):
	list_display = ('community', 'need_rental_agreement')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]
class TypeAdmin (admin.ModelAdmin):
	list_display = ('note', 'price_per_month')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]
class QueueAdmin (admin.ModelAdmin):
	list_display = ('community', 'user', 'note_queue')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]

admin.site.register(Area, AreaAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Queue, QueueAdmin)
admin.site.register(Transaction, TransactionAdmin)


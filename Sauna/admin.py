from Sauna.models import Sauna, Time_slot, Sauna_queue, Sauna_transaction
from django.contrib import admin

class SaunaAdmin(admin.ModelAdmin):
	list_display = ('name', 'community',)
	list_filter = ( 'community__city', 'community__postal_code',)
	search_fields = ('community__address', 'community__city', 'community__postal_code','name')

	fieldsets = [
			('Sauna information',			{'fields': ['name','community']}),
			('Additional information', 		{'fields': ['note']}),

	  			]

class TimeAdmin(admin.ModelAdmin):
	list_display = ('name', 'sauna','is_free',)
	list_filter = ( 'sauna__community__city', 'sauna__community__postal_code', 'sauna__name')
	search_fields = ('sauna__community__address', 'sauna__community__city', 'sauna__community__postal_code','name')

	fieldsets = [
			('TimeSlot information',			{'fields': ['name','sauna',]}),
			('Additional information', 		{'fields': ['note',]}),

	  			]


class S_QueueAdmin(admin.ModelAdmin):
	list_display = ('community', 'user', 'register_date', 'note')
	list_filter = ('community__city', 'community__postal_code')
	search_fields = ('community__city', 'community__address', 'community__postal_code', 'user__last_name', 'user__first_name')

	fieldsets = [
			('Sauna queue information',		{'fields': ['user','community',]}),
			('Additional information', 		{'fields': ['note',]}),

	  			]

class S_TransactionAdmin(admin.ModelAdmin):
	#list_display = ('sauna_slot', 'sauna_queue__community__name', 'sauna_queue__user__name', 'start_date', 'end_date',)
	list_filter = ('sauna_queue__community__city', 'end_date',)
	#Display doesn't work because it sucks

	fieldsets = [
			('Timeslot information',		{'fields': ['sauna_slot',]}),
			('Queue information', 			{'fields': ['sauna_queue',]}),
			('Date information',			{'fields': ['end_date', ]}),
			('Additional information', 		{'fields': ['note',]}),

	  			]
	
admin.site.register(Sauna, SaunaAdmin)
admin.site.register(Time_slot, TimeAdmin)
admin.site.register(Sauna_queue, S_QueueAdmin)
admin.site.register(Sauna_transaction, S_TransactionAdmin)
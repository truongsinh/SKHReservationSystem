from Sauna.models import Sauna, Time_slot
from django.contrib import admin

class SaunaAdmin(admin.ModelAdmin):
	list_display = ('name', 'community',)
	list_filter = ('community__address', 'community__city', 'community__postal_code','name')
	search_fields = ('community__address', 'community__city', 'community__postal_code','name')

	fieldsets = [
			('Sauna information',			{'fields': ['name','community']}),
			('Additional information', 		{'fields': ['note']}),

	  			]

class TimeAdmin(admin.ModelAdmin):
	list_display = ('name', 'sauna',)
	list_filter = ('sauna__community__address', 'sauna__community__city', 'sauna__community__postal_code','name')
	search_fields = ('sauna__community__address', 'sauna__community__city', 'sauna__community__postal_code','name')

	fieldsets = [
			('TimeSlot information',			{'fields': ['name','sauna',]}),
			('Additional information', 		{'fields': ['note',]}),

	  			]



admin.site.register(Sauna, SaunaAdmin)
admin.site.register(Time_slot, TimeAdmin)
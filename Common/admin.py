from Common.models import Community, Apartment, Profile
from django.contrib import admin

class CommunityAdmin (admin.ModelAdmin):
	list_display = ('address', 'note')
	search_fields = ('address',)
	fieldsets = [
	('Community address',	{'fields': ['address']}),
	('Note', 				{'fields': ['note']}),
	]

class ApartmentAdmin (admin.ModelAdmin):
	list_display = ('community', 'address')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]

class ProfileAdmin (admin.ModelAdmin):
	list_display = ('user', 'apartment', 'plate_no')
fieldsets = [
	('',				{'fields': ['']}),
	('', 				{'fields': ['']}),
		]

admin.site.register(Community, CommunityAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Profile, ProfileAdmin)

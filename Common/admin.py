from Common.models import Community, Apartment, Profile
from django.contrib import admin

class CommunityAdmin (admin.ModelAdmin):
	list_display = ('address', 'postal_code', 'city',)
	search_fields = ('address', 'city', 'postal_code',)
	list_filter    = ('city', 'postal_code')
	fieldsets = [
	('Community address',	{'fields': ['address','postal_code', 'city']}),
	('Additional information', 				{'fields': ['note']}),
	]

class ApartmentAdmin (admin.ModelAdmin):
	list_display = ('community', 'address' )
	list_filter    = ('community', )
	fieldsets = [
	('Address information',				{'fields': ['community', 'address']}),
	('Additional information', 				{'fields': ['note']}),
		]

class ProfileAdmin (admin.ModelAdmin):
	list_display = ('first_name', 'apartment', 'plate_no')
	fieldsets = [
	('User information',				{'fields': ['first_name','apartment', 'plate_no']}),
	('Additional information', 				{'fields': ['note']}),
		]

admin.site.register(Community, CommunityAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Profile, ProfileAdmin)

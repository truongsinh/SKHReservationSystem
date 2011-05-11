from django.contrib.auth.admin import UserAdmin
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
	list_filter = ( 'community__city', 'community__postal_code',)
	search_fields = ('community__address', 'community__city', 'community__postal_code','address')

	fieldsets = [
	('Address information',				{'fields': ['community', 'address']}),
	('Additional information', 				{'fields': ['note']}),
		]

class ProfileAdmin (admin.ModelAdmin):
#class ProfileAdmin (UserAdmin):
	list_display = ('last_name', 'first_name', 'apartment', 'plate_no')
	list_filter = ('apartment__community__city', 'apartment__community__postal_code',)
	search_fields = ('apartment__community__city', 'apartment__community__postal_code', 'apartment__community__address', 'plate_no','first_name', 'last_name', )

	fieldsets = [
					('User information',
						{
							'fields': [
								'first_name',
								'last_name',
								'apartment',
								'plate_no',
								'username',
								'email',
							]
						}
					),
					('Permissions',
						{
							'fields': [
								'is_active',
								'is_staff',
								'is_superuser',
								'user_permissions',
							]
						}
					),
					('Important dates',
						{
							'fields': [
								'date_joined',
								'last_login',
							]
						}
					),
					('Groups',
						{
							'fields': [
								'groups',
							]
						}
					),
					('Additional information',
						{
							'fields': [
								'note'
							]
						}
					),
				]
	#Password change form doesn't work when using admin interface and changing the password from Profile
admin.site.register(Community, CommunityAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Profile, ProfileAdmin)

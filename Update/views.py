# Create your views here.
from django.http import HttpResponse
from django.core import management
from settings import DEBUG

if DEBUG:
	#
	def update(request):
		from Common.models import Community, Apartment, Profile;from django.contrib.auth.models import User
		response = ""

		#flush all the data in database
		response += ">>> manage.py flush<br />"
		management.call_command('flush', verbosity=1, interactive=False)


		#create instances for Common model


		response += '>>> u1 = User();u1.username = "admin";u1.is_staff = True;u1.is_active = True;u1.is_superuser = True;u1.set_password("admin");u1.save()<br />'
		u1 = User();u1.username = "admin";u1.is_staff = True;u1.is_active = True;u1.is_superuser = True;u1.set_password("admin");u1.save()

		response += '>>> u2 = User();u2.username = "admin2";u2.is_staff = True;u2.is_active = True;u2.is_superuser = True;u2.set_password("admin2");u2.save()<br />'
		u2 = User();u2.username = "admin2";u2.is_staff = True;u2.is_active = True;u2.is_superuser = True;u2.set_password("admin2");u2.save()

		response += '>>> c1 = Community.objects.get_or_create(address="ExampleRoad 15 Lahti")[0]<br />'
		c1 = Community.objects.get_or_create(address="ExampleRoad 15 Lahti")[0]

		response += '>>> a1 = Apartment.objects.get_or_create(community = c1, address = "42B", note = "This is just a normal note." )[0]<br />'
		a1 = Apartment.objects.get_or_create(community = c1, address = "42B", note = "This is just a normal note." )[0]

		response += '>>> p1 = Profile.objects.get_or_create(user = u, apartment = a1, plate_no = "TIS-517")[0]<br />'
		p1 = Profile(apartment = a1, plate_no = "TIS-517");p1.user_id = 1;p1.save()
		return HttpResponse(response)
else:
	def update(request):
		return HttpResponse("Invalid")
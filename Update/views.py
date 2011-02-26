# Create your views here.
from django.http import HttpResponse
from django.core import management
from Parking.models import Area, Type, Slot
from settings import DEBUG

if DEBUG:
	#
	def update(request):
		from Common.models import Community, Apartment, Profile;from django.contrib.auth.models import User
		response = ""
		#flush all the data in database
		response += "Flushing database<br />"
		management.call_command('flush', verbosity=1, interactive=False)

		#creating GROUP??? config permissions




		response += 'Creating COMMUNITY 1<br />'
		c1 = Community.objects.get_or_create(address="ExampleRoad 15 Lahti")[0]

		response += 'Creating COMMUNITY 2<br />'
		c2 = Community.objects.get_or_create(address="ExampleRoad 152 Turku")[0]

		response += 'Creating APARTMENT 1<br />'
		a1 = Apartment.objects.get_or_create(community = c1, address = "42B", note = "This is just a normal note." )[0]

		response += 'Creating APARTMENT 2<br />'
		a2 = Apartment.objects.get_or_create(community = c1, address = "37F", note = "Another note" )[0]

		response += 'Creating USER admin<br />'
		u1 = User()
		u1.username = "admin"
		u1.set_password("admin")
		u1.first_name = "Kari"
		u1.last_name = "Tran"
		u1.email = "truongsinh.tran@gmail.com"
		u1.is_staff = True
		u1.is_active = True
		u1.is_superuser = True
		u1.save()
		response += 'Creating PROFILE 1<br />'
		p1 = Profile(apartment = a1, plate_no = "TIS-517")
		p1.user_id = 1
		p1.save()

		#Creating more PROFILE
		response += 'Creating USER admin2<br />'
		u2 = User()
		u2.username = "admin2"
		u2.set_password("admin2")
		u2.first_name = "Vinh"
		u2.last_name = "Nguyen"
		u2.email = "ngvinh47@gmail.com"
		u2.is_staff = True
		u2.is_active = True
		u2.is_superuser = True
		u2.save()


		response += 'Creating AREA 1<br />'
		a1 = Area()
		a1.community = c1
		a2.note = "AREA 1"
		a1.need_rental_agreement = True
		a1.save()
		a1.user_in_charge.add(u1)
		a1.user_in_charge.add(u2)

		response += 'Creating AREA 2<br />'
		a2 = Area()
		a2.community_id = 2
		a2.need_rental_agreement = False
		a2.note = "JDFLDF"
		a2.save()
		a2.user_in_charge.add(u1)

		response += 'Creating TYPE roofair<br />'
		roofair = Type()
		roofair.community = c1
		roofair.Area = a1
		roofair.parking_area_id = 1
		roofair.price_per_month = "50"
		roofair.note = "SADFDF"
		roofair.save()

		response += 'Creating TYPE openair<br />'
		openair = Type()
		openair.community = c1
		openair.Area = a1
		openair.parking_area_id = 2
		openair.price_per_month = "30"
		openair.note = "asdfsdf"
		openair.save()

		response += 'Creating SLOT 1<br />'
		Slot1 = Slot()
		Slot1.parking_area_id = 2
		Slot1.parking_type = openair
		Slot1.note = "ASDFSDF"
		Slot1.save()

		#Creting QUEUE

		#Creating TRANSACTION

		return HttpResponse(response)
else:
	def update(request):
		return HttpResponse("Invalid")
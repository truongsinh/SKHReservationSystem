# Create your views here.
from django.http import HttpResponse
from django.core import management
from Parking.models import Area, Type, Slot, Queue, Transaction
from settings import DEBUG

if DEBUG:
	#
	def update(request):
		from Common.models import Community, Apartment, Profile;from django.contrib.auth.models import User
		response = ""
		#flush all the data in database
		response += "Flushing database<br />"
		management.call_command('flush', verbosity=1, interactive=False)


		response += 'Creating COMMUNITY 1<br />'
		c1 = Community.objects.get_or_create(address="ExampleRoad 15 Lahti")[0]

		response += 'Creating COMMUNITY 2<br />'
		c2 = Community.objects.get_or_create(address="ExampleRoad 152 Turku")[0]

		response += 'Creating APARTMENT 1<br />'
		a1 = Apartment.objects.get_or_create(community = c1, address = "42B", note = "This is just a normal note." )[0]

		response += 'Creating APARTMENT 2<br />'
		a2 = Apartment.objects.get_or_create(community = c1, address = "37F", note = "Another note" )[0]

		
		#creating GROUP??? config permissions
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

		#Creating PROFILE for user 2
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

		#Creating PROFILE for user 3 - SKH staff
		response += 'Creating USER SKH staff 1<br />'
		u3 = User()
		u3.username = "skh1"
		u3.set_password("skh1")
		u3.first_name = "Jussi"
		u3.last_name = "Penttinen"
		u3.email = "jussi.penttinen@lpt.fi"
		u3.is_staff = True
		u3.is_active = True
		u3.is_superuser = True
		u3.save()
		
		#Creating PROFILE for user 4 - SKH staff
		response += 'Creating USER SKH staff 2<br />'
		u4 = User()
		u4.username = "skh2"
		u4.set_password("skh2")
		u4.first_name = "Sirak"
		u4.last_name = "Kebele"
		u4.email = "sirak77@gmail.fi"
		u4.is_staff = True
		u4.is_active = True
		u4.is_superuser = True
		u4.save()

		#creating area 1 in community 1
		response += 'Creating AREA 1<br />'
		a1 = Area()
		a1.community = c1
		a1.note = "AREA 11"
		a1.need_rental_agreement = True
		a1.save()
		a1.user_in_charge.add(u1)
		a1.user_in_charge.add(u2)
		#creating area 2 in community 1
		response += 'Creating AREA 12<br />'
		a2 = Area()
		a2.community_id = 2
		a2.need_rental_agreement = False
		a2.note = "AREA12"
		a2.save()
		a2.user_in_charge.add(u1)

		#creating area 1 in community 2
		response += 'Creating AREA 21<br />'
		a3 = Area()
		a3.community = c2
		a3.need_rental_agreement = True
		a3.note = "AREA21"
		a3.save()
		a3.user_in_charge.add(u2)
		#creating area 2 in community 2
		response += 'Creating AREA 22<br />'
		a4 = Area()
		a4.community = c2
		a4.need_rental_agreement = False
		a4.note = "AREA22"
		a4.save()
		a4.user_in_charge.add(u1)

		#creating TYPE in Area 1 in Community 1
		response += 'Creating TYPE rooftop<br />'
		rooftop = Type()
		rooftop.community = c1
		rooftop.Area = a1
		rooftop.parking_area_id = 1
		rooftop.price_per_month = "50"
		rooftop.note = "SADFDF"
		rooftop.save()

		#creating TYPE in Area 2 in Community 1
		response += 'Creating TYPE openair<br />'
		openair = Type()
		openair.community = c1
		openair.Area = a1
		openair.parking_area_id = 2
		openair.price_per_month = "30"
		openair.note = "asdfsdf"
		openair.save()

		#creating TYPE in Area 1 in Community 2
		response += 'Creating TYPE rooftop<br />'
		rooftop = Type()
		rooftop.community = c2
		rooftop.Area = a3
		rooftop.parking_area_id = 1
		rooftop.price_per_month = "50"
		rooftop.note = "SADFDF"
		rooftop.save()

		#creating TYPE in Area 2 in Community 2
		response += 'Creating TYPE openair<br />'
		openair = Type()
		openair.community = c2
		openair.Area = a4
		openair.parking_area_id = 2
		openair.price_per_month = "30"
		openair.note = "asdfsdf"
		openair.save()

		#creating slot1 in parking_area_2
		response += 'Creating SLOT 1<br />'
		Slot1 = Slot()
		Slot1.parking_area_id = 1
		Slot1.parking_type = rooftop
		Slot1.note = "ASDFSDF"
		Slot1.save()

		#creating slot2 in parking_area_2
		response += 'Creating SLOT 2<br />'
		Slot2 = Slot()
		Slot2.parking_area_id = 1
		Slot2.parking_type = openair
		Slot2.note = "ASDOFNDFKF464"
		Slot2.save()

		#creating slot3 in parking_area_1
		response += 'Creating SLOT 3<br />'
		Slot3 = Slot()
		Slot3.parking_area_id = 2
		Slot3.parking_type = openair
		Slot3.note = "Aadsf979912"
		Slot3.save()

		#creating slot2 in parking_area_2
		response += 'Creating SLOT 4<br />'
		Slot4 = Slot()
		Slot4.parking_area_id = 2
		Slot4.parking_type = openair
		Slot4.note = "ASDdfd44616"
		Slot4.save()


		#Creting QUEUE
		#creating queue1 for community 1
		response += 'Creating QUEUE <br />'
		q1 = Queue()
		q1.community = c1
		q1.user_id = 1
		q1.register_date = "10.12.10"
		q1.decision_date = "12.12.10"
		q1.decision = True
		q1.note = "user 1 is registered"
		q1.save()

		#creating queue2 for community 2
		response += 'Creating QUEUE <br />'
		q2 = Queue()
		q2.community = c2
		q2.user_id = 2
		q2.register_date = "11.2.11"
		q2.decision_date = "14.2.11"
		q2.decision = True
		q2.note = "user 2 is registered"
		q2.save()

		#Creating TRANSACTION
		#creating transaction for user 1 in community 1
		t1 = Transaction()
		t1.community = c1 # Community? Area?
		t1.area = a1
		t1.user = u1
		#t1.queue = q1 # ???? or reservation list
		t1.type = rooftop
		t1.slot = Slot1
		t1.start_date = "13.12.10"
		t1.end_date = "29.12.10"
		t1.paid = True
		t1.note = "u1: already paid"
		t1.save()

		#creating transaction for user 2 community 2
		t2 = Transaction()
		t2.community = c2 # Community? Area?
		t2.area = a2
		t2.user = u2
		#t2.queue = q2 # ???? or reservation list
		t2.type = openair
		t2.slot = Slot3
		t2.start_date = "15.2.11"
		t2.end_date = "29.3.11"
		t2.paid = False
		t2.note = "Reminder for u2 to pay the invoice"
		t2.save()

		return HttpResponse(response)
else:
	def update(request):
		return HttpResponse("Invalid")
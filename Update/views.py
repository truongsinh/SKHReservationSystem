# Create your views here.
from django.http import HttpResponse
from settings import DEBUG

if DEBUG:
	#
	def update(request):
		from django.core import management
		from django.contrib.auth.models import User, Group, Permission
		from Common.models import *
		from Parking.models import *
		response = ""
		#flush all the data in database
		response += "Flushing database<br />"
		management.call_command('flush', verbosity=1, interactive=False)


		response += 'Creating COMMUNITY 1<br />'
		c1 = Community.objects.get_or_create(address="ExampleRoad 15", city="Lahti", postal_code="15110")[0]

		response += 'Creating COMMUNITY 2<br />'
		c2 = Community.objects.get_or_create(address="ExampleRoad 152 Turku")[0]

		response += 'Creating APARTMENT 1<br />'
		a1 = Apartment.objects.get_or_create(community = c1, address = "42B", note = "This is just a normal note." )[0]

		response += 'Creating APARTMENT 2<br />'
		a2 = Apartment.objects.get_or_create(community = c1, address = "37F", note = "Another note" )[0]

		#creating GROUP??? config permissions
		response += 'Creating GROUP for users<br />'
		#creating group name
		g1 = Group(name = 'SKH Staff/ admin')

		#creating group permissions
		#p1 = Permission.objects.create('')
		#add permissions to the group
		g1.save()
		#g1.permissions.add(p1)


		response += 'Creating USER admin<br />'
		u1 = Profile()
		u1.username = "admin"
		u1.set_password("admin")
		u1.first_name = "Kari"
		u1.last_name = "Tran"
		u1.email = "truongsinh.tran@gmail.com"
		u1.is_staff = True
		u1.is_active = True
		u1.is_superuser = True
		u1.apartment = a1
		u1.plate_no = "TIS-517"
		#u1.user_permissions.add('SKHReservationSystem.add_Community')
		u1.save()
		u1.groups.add(g1)
		u1.has_perm('SKHReservationSystem.add_Common.community')

		#Creating PROFILE for user 2 fgfgfg
		response += 'Creating USER admin2<br />'
		u2 = Profile()
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
		u3 = Profile()
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
		u4 = Profile()
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
		rooftop.price_per_month = "50"
		rooftop.note = "SADFDF"
		rooftop.save()

		#creating TYPE in Area 2 in Community 1
		response += 'Creating TYPE openair<br />'
		openair = Type()
		openair.price_per_month = "30"
		openair.note = "asdfsdf"
		openair.save()

		#creating TYPE in Area 1 in Community 2
		response += 'Creating TYPE rooftop<br />'
		rooftop = Type()
		rooftop.price_per_month = "50"
		rooftop.note = "SADFDF"
		rooftop.save()

		#creating TYPE in Area 2 in Community 2
		response += 'Creating TYPE openair<br />'
		openair = Type()
		openair.price_per_month = "30"
		openair.note = "asdfsdf"
		openair.save()

		#creating slot1 in parking_area_2
		response += 'Creating SLOT 1<br />'
		Slot1 = Slot()
		Slot1.parking_area = a1
		Slot1.parking_type = rooftop
		Slot1.note = "ASDFSDF"
		Slot1.save()
		response += 'Creating SLOT 1<br />'

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
		q1.user_id = 1
		q1.community = c1
		q1.decision_date = "2011-06-14"
		q1.decision = True
		q1.note_queue = "user 1 is registered"
		#q1.save()

		#creating queue2 for community 2
		response += 'Creating QUEUE <br />'
		q2 = Queue()
		q2.community = c2
		q2.user_id = 2
		q2.decision = False
		q2.note_queue = "user 2 is registered"
		q2.save()

		#Creating TRANSACTION
		'''
	user = models.ForeignKey(User)
	community = models.ForeignKey(Community)
	register_date = models.DateField('Registered Date', auto_now_add=True)
	decision_date = models.DateField('Decided Date', blank=True, null=True)

	parking_slot = models.ForeignKey(Slot)
	parking_queue = models.ForeignKey(Queue)
	start_date = models.DateField('Start Date', auto_now_add=True)
	end_date = models.DateField('End Date', blank=True, null=True)
	paid = models.BooleanField()
	note = models.TextField(max_length=127)'''


		#creating transaction for user 1 in community 1
		t1 = Transaction()
		#
		t1.id = q1.id
		t1.user = q1.user
		t1.community = q1.community
		t1.register_date = q1.register_date
		t1.decision_date = q1.decision_date
		t1.note_queue = q1.note_queue
		#
		t1.parking_slot = Slot1
		t1.paid = True
		t1.note_transaction = "u1: already paid"
		t1.save()

		#creating transaction for user 2 community 2
		t2 = Transaction()
		#
		t2.id = q2.id
		t2.user = q2.user
		t2.community = q2.community
		t2.register_date = q2.register_date
		t2.decision_date = q2.decision_date
		t2.note_queue = q2.note_queue
		#
		t2.parking_slot = Slot3
		t2.start_date = "2011-11-06"
		t2.end_date = "2011-12-19"
		t2.paid = False
		t2.note_transaction = "Reminder for u2 to pay the invoice"
		t2.save()

		return HttpResponse(response)
else:
	def update(request):
		return HttpResponse("Invalid")
# Create your views here.
from django.http import HttpResponse
from settings import DEBUG
from django.contrib.auth.models import User, Group, Permission
from Common.models import *
from Parking.models import *

if DEBUG:
	#
	def update(request):
		from django.core import management
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

		response += 'Creating USER1 in SKHStaff/admin<br />'
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
		u1.save()

		#Creating PROFILE for user 2
		response += 'Creating USER2 in SKHStaff/admin<br />'
		u2 = Profile()
		u2.username = "admin2"
		u2.set_password("admin2")
		u2.first_name = "Vinh"
		u2.last_name = "Nguyen"
		u2.email = "ngvinh47@gmail.com"
		u2.is_staff = True
		u2.is_active = True
		u2.is_superuser = False
		u2.save()

		#Creating PROFILE for user 3 - Board of Community
		response += 'Creating USER3 in Board of Community<br />'
		u3 = Profile()
		u3.username = "board1"
		u3.set_password("board1")
		u3.first_name = "Jussi"
		u3.last_name = "Penttinen"
		u3.email = "jussi.penttinen@lpt.fi"
		u3.is_staff = True
		u3.is_active = True
		u3.is_superuser = False
		u3.save()

		#Creating PROFILE for user 4 - Traffic warden
		response += 'Creating USER4 in Traffic warden<br />'
		u4 = Profile()
		u4.username = "traffic1"
		u4.set_password("traffic1")
		u4.first_name = "Sirak"
		u4.last_name = "Kebele"
		u4.email = "sirak77@gmail.fi"
		u4.is_staff = True
		u4.is_active = True
		u4.is_superuser = False
		u4.save()

		#Creating PROFILE for user 5 - Residents
		response += 'Creating USER5 in Residents<br />'
		u5 = Profile()
		u5.username = "resident1"
		u5.set_password("resident1")
		u5.first_name = "sadfodjf"
		u5.last_name = "sgfgdf"
		u5.email = "adfdf@gmail.fi"
		u5.is_staff = False
		u5.is_active = True
		u5.is_superuser = False
		u5.save()
		'''
		#Creating PROFILE for user 6 - Guest
		response += 'Creating PROFILE 6 in Residents<br />'
		u6 = Profile()
		u6.username = "guest1"
		u6.set_password("guest1")
		u6.first_name = "sdf"
		u6.last_name = "jkj4"
		u6.email = "dfd8@gmail.fi"
		u6.is_staff = True
		u6.is_active = True
		u6.is_superuser = True
		u6.save()
		'''
		#creating area 1 in community 1
		response += 'Creating AREA 11<br />'
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
		a3.name = "name 1"
		a3.community = c2
		a3.need_rental_agreement = True
		a3.note = "AREA21"
		a3.save()
		a3.user_in_charge.add(u2)
		#creating area 2 in community 2
		response += 'Creating AREA 22<br />'
		a4 = Area()
		a4.name = "name 2"
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
		response += 'Creating TYPE openair <br />'
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
		Slot2.name = "name 1"
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
		Slot4.name = "name 1"
		Slot4.parking_area_id = 2
		Slot4.parking_type = openair
		Slot4.note = "ASDdfd44616"
		Slot4.save()


		#Creting QUEUE
		#creating queue1 for community 1
		response += 'Creating QUEUE 1 <br />'
		q1 = Queue()
		q1.community = c1
		q1.user_id = 1
		q1.decision_date = "2011-06-14"
		q1.decision = True
		q1.note = "user 1 is registered"
		q1.save()

		#creating queue2 for community 2
		response += 'Creating QUEUE 2<br />'
		q2 = Queue()
		q2.community = c2
		q2.user_id = 2
		q2.decision = False
		q2.note = "user 2 is registered"
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
		#t1.parking_slot = Slo
		#t1.area = a1
		#t1.user = u1
		#t1.queue = q1 # ???? or reservation list
		t1.type = rooftop
		t1.parking_slot = Slot1
		t1.start_date = "2011-03-08"
		t1.end_date = "2011-08-09"
		t1.paid = True
		t1.note = "u1: already paid"
		#t1.save()

		#creating transaction for user 2 community 2
		t2 = Transaction()
		t2.community = c2 # Community? Area?
		t2.area = a2
		t2.user = u2
		#t2.queue = q2 # ???? or reservation list
		t2.type = openair
		t2.parking_slot = Slot3
		t2.start_date = "2011-11-06"
		t2.end_date = "2011-12-19"
		t2.paid = False
		t2.note = "Reminder for u2 to pay the invoice"
		#t2.save()

		#creating GROUP??? config permissions
		response += 'Creating GROUP for users<br />'
		#creating group name
		g1 = Group(name = 'SKH Staff')
		g1.save()
		g2 = Group(name = 'Residents')
		g2.save()
		g3 = Group(name = 'Board of Community')
		g3.save()
		g4 = Group(name = 'Traffic warden')
		g4.save()
		#g5 = Group(name = 'Guest')
		#g5.save()
		#creating permissions for models in Common app
		#add
		#change
		#delete
		#view
		#	view_full
		#	view_last_name
		#	view_something
		#creating permissions for apartment model
		view_apartment	= Permission.objects.get(codename='view_apartment')
		change_apartment= Permission.objects.get(codename='change_apartment')

		#creating permissions for community model
		view_community	= Permission.objects.get(codename='view_community')
		'''
		change_community = Permission.objects.get_or_create(name='Can change community', codename='change_community',
                       content_type=community_per)[0]

		#creating permissions for profile model
		profile_per = ContentType.objects.get(app_label='Common', model='profile')
		view_profile = Permission.objects.get_or_create(name='Can view profile', codename='view_profile',
                       content_type=profile_per)[0]
		change_profile = Permission.objects.get_or_create(name='Can change profile', codename='change_profile', content_type=profile_per)[0]

#creating permissions for models in Parking app
		#creating permissions for area model
		area_per = ContentType.objects.get(app_label='Parking', model='area')
		view_area = Permission.objects.get_or_create(name='Can view area', codename='view_area',
                       content_type=area_per)[0]
		change_area = Permission.objects.get_or_create(name='Can change area', codename='change_area',
                       content_type=area_per)[0]
		#creating permissions for type model
		type_per = ContentType.objects.get(app_label='Parking', model='type')
		view_type = Permission.objects.get_or_create(name='Can view type', codename='view_type',
                       content_type=type_per)[0]
		change_type = Permission.objects.get_or_create(name='Can change type', codename='change_type',
                       content_type=type_per)[0]
		#creating permissions for slot model
		slot_per = ContentType.objects.get(app_label='Parking', model='slot')
		view_slot = Permission.objects.get_or_create(name='Can view slot', codename='view_slot',
                       content_type=slot_per)[0]
		change_slot = Permission.objects.get_or_create(name='Can change slot', codename='change_slot',
                       content_type=slot_per)[0]
		#creating permissions for queue model
		queue_per = ContentType.objects.get(app_label='Parking', model='queue')
		view_queue = Permission.objects.get_or_create(name='Can view queue', codename='view_queue',
                       content_type=queue_per)[0]
		change_queue = Permission.objects.get_or_create(name='Can change queue', codename='change_queue',
                       content_type=queue_per)[0]
		#creating permissions for transaction model
		transaction_per = ContentType.objects.get(app_label='Parking', model='transaction')
		view_transaction = Permission.objects.get_or_create(name='Can view transaction', codename='view_transaction',
                       content_type=transaction_per)[0]
		change_transaction = Permission.objects.get_or_create(name='Can change transaction', codename='change_transaction',
                       content_type=transaction_per)[0]

		
		#assigning permission to each group
		#Group 1 - SKHStaff
		g1.permissions.add(view_apartment)
		g1.permissions.add(view_community)
		g1.permissions.add(view_profile)
		g1.permissions.add(view_area)
		g1.permissions.add(view_type)
		g1.permissions.add(view_slot)
		g1.permissions.add(view_queue)
		g1.permissions.add(view_transaction)
		g1.permissions.add(change_apartment)
		g1.permissions.add(change_community)
		g1.permissions.add(change_profile)
		g1.permissions.add(change_area)
		g1.permissions.add(change_type)
		g1.permissions.add(change_slot)
		g1.permissions.add(change_queue)
		g1.permissions.add(change_transaction)
		#Group 2 - Residents
		g2.permissions.add(view_apartment)
		g2.permissions.add(view_community)
		g2.permissions.add(view_profile)
		g2.permissions.add(view_area)
		g2.permissions.add(view_type)
		g2.permissions.add(view_slot)
		g2.permissions.add(view_queue)
		g2.permissions.add(view_transaction)

		# Group 3 - Board of Community
		g3.permissions.add(view_apartment)
		g3.permissions.add(view_community)
		g3.permissions.add(view_profile)
		g3.permissions.add(view_area)
		g3.permissions.add(view_type)
		g3.permissions.add(view_slot)
		g3.permissions.add(view_queue)
		g3.permissions.add(view_transaction)
		# Group 4 - Traffic warden
		g4.permissions.add(view_apartment)
		g4.permissions.add(view_community)
		g4.permissions.add(view_profile)
		g4.permissions.add(view_area)
		g4.permissions.add(view_type)
		g4.permissions.add(view_slot)
		g4.permissions.add(view_queue)
		g4.permissions.add(view_transaction)
		'''		# Group 5 - Guests
		#assigning users to each group
		u1.groups.add(g1)
		u2.groups.add(g1)
		u3.groups.add(g3)
		u4.groups.add(g4)
		u5.groups.add(g2)
		#u6.groups.add(g5)

		#checking user permissions
		u1.has_perm('Common.view_apartment')
		# True
		u2.has_perm('Common.change_community')
		#True
		u3.has_perm('Common.change_area')
		#False
		u4.has_perm('Common.view_apartment')
		#True
		u5.has_perm('Common.view_queue')

		return HttpResponse(response)
else:
	def update(request):
		return HttpResponse("Invalid")
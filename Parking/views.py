# Create your views here.
# .../parking/parking_area_id/parking_type_id/parking_slot_id

# 3. reservation_list (request, transaction_id, GET)
#	user last name, plate number, star date, end date (each link to transaction_detail - 4)
# 4. history_list (request, transaction_id, GET)
#	user last name, plate number, star date, end date (each link to transaction_detail - 4)
# 5. transaction_detail (request, transaction_id, GET)
#	all the information, link back to???
# 5. queue_list (request, community_id, GET)
# 6. queue_detail (request, community_id, GET)
# 7. add_queue (request, POST)
# 8.



# view for admin
# 1. update (request, user_id, POST)
# 2. update (request, parking_slot_id, POST)
# 3. update (request, parking_transaction_id, POST)
# 4. update (request, parking_parking_area_id, POST)
# 5. update (request, parking_type_id, POST)
# 6. update (request, common_profile_id, POST)
# 7. LockSlot (request, parking_slot_id, POST)
# 8. Invoice (request, user_id, GET)
# 9. reservation (request, community_id, POST)
# 10. reservation (request, community_id, GET)
# 11. queue (request, community_id, POST)
# 12. queue (request, community_id, GET)
# URL
# (r'parking_slot/$', 'index'), ....
# (r'^parking_slot/(?P<parking_slot_id>\d+)/$', 'detail'),
# (r'^parking_area/(?P<parking_area_id>\d+)/$', 'detail'),
# (r'^parking_area/(?P<parking_area_id>\d+)/$', 'reservation'),
# (r'^parking_area/(?P<parking_area_id>\d+)/$', 'queue'),



# view for board of community
# 1. 
# 2. 
# 3. 


# view for maintenance service/ janitor


# view for traffic warden
# 1. reservation


# view for users
# 1. account (request, user_id, GET)
# 2. updateacc (request, user_id, POST)
# 3. reservation (request, community_id, GET)
# 4. cancel (request, community_id, POST)
# 5. homepageinfo ()
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django import forms
from Common.models import Community
from Parking.models import Queue, Transaction

def index(request, community_id):
	return render_to_response('Parking/index.html')

def queue_list(request, community_id, page):
	queue_list = Queue.objects.filter(community = community_id)
	return render_to_response('Parking/queue_list.html',{'queue_list': queue_list })

def queue_detail(request, queue_id):
	q = Queue.objects.get(id=queue_id)
	u = q.user
	return render_to_response('Parking/queue_detail.html', {'u':u, 'q':q,}, )

def reservation_list(request, community_id, page):
	reservation_list = Transaction.objects.filter(parking_queue__community = community_id)
	return render_to_response('Parking/reservation_list.html', {'reservation_list': reservation_list })


def reservation_add(request):
	return render_to_response('Parking/reservation_add.html')

def reservation_detail(request, transaction_id):
	#t = Transaction.parking_queue.
	
	
	return render_to_response('Parking/reservation_detail.html')


def area_list(request, community_id, page):
	return render_to_response('Parking/area_list.html')

def area_detail(request, area_id):
	return render_to_response('Parking/area_detail.html')
# Create your views here.
# .../parking/parking_area_id/parking_type_id/parking_slot_id

# common view (read only)
# 1. index (request, community_id, GET)
# 2. detail (request, community_id, GET)
# 3. reservation (request, community_id, GET)
# 4. queue (request, community_id, GET)


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



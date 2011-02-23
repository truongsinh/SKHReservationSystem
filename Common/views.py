# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from Common.models import Community, Apartment, Profile
from Parking.models import Queue
# 1. community_list (request, community_id, GET)
#	community_address (list)
# 2. community_detail (request, community_id, GET)
#	link to reservation list (3)
#	link to queue list (4)
#	form to apply for parking queue (send POST request to add_queue (7))

def community_list(request):
	# pagination later
    community_list = Community.objects.all().order_by('address')
    return render_to_response('Common/community_list.html', {'community_list': community_list })

def community_detail (request, community_id):
    c = get_object_or_404(Community, pk=community_id)
    return render_to_response('Common/community_detail.html', {'Community':c},
                              context_instance=RequestContext(request))
    
#def community_detail(request):
#	return HttpResponseRedirect(reverse('Common.community.views.resul', args=(community.id,)))


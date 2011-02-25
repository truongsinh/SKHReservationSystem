# Create your views here.
from django.core.urlresolvers import reverse
from django.forms.widgets import HiddenInput
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from Common.models import Community, Apartment, Profile
from django import forms
# 1. community_list (request, community_id, GET)
#	community_address (list)
# 2. community_detail (request, community_id, GET)
#	link to reservation list (3)
#	link to queue list (4)
#	form to apply for parking queue (send POST request to add_queue (7))
import Parking


def community_list(request):
	# pagination later
	community_list = Community.objects.all().order_by('address')
	return render_to_response('Common/community_list.html', {'community_list': community_list })

def community_detail(request, community_id):
	c = get_object_or_404(Community, pk=community_id)
	class queue_add_form(forms.Form):
		community = forms.ModelChoiceField(queryset=Community.objects.all(), initial=community_id)
		note = forms.CharField(widget=forms.Textarea)
	f = queue_add_form()
	l = reverse(Parking.views.queue_add)
	s = 'Register'
	r = reverse('Parking.views.reservation_list', args=[c.id])
	q = reverse('Parking.views.queue_list', args=[c.id])
 	return render_to_response('Common/community_detail.html',
							  {
								'community':c,
								'form':f,
								'action':l,
								'submit':s,
								'reservation':r,
								'queue':q,
								},
                              context_instance=RequestContext(request),
							  )

def community_detail(request, community_id):
	return HttpResponseRedirect(reverse('<a href="Common/community_detail/1945">Reservation list</a>' ))




def profile(request, user_id):
	return render_to_response(reverse('Common/profile.html'))

# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
# 1. community_list (request, community_id, GET)
#	community_address (list)
# 2. community_detail (request, community_id, GET)
#	link to reservation list (3)
#	link to queue list (4)
#	form to apply for parking queue (send POST request to add_queue (7))
from Common.models import Community
import Parking
from  django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

'''class UserForm:
	f = AuthenticationForm
	return f'''

@login_required(login_url='/reservation/login/')
def community_list(request, page):
	# pagination later
	community_list = Community.objects.all().order_by('address')
	return render_to_response('Common/community_list.html', {'community_list': community_list })

@login_required(login_url='/reservation/login/')
def community_detail(request, community_id):
	c = get_object_or_404(Community, pk=community_id)
	class queue_add_form(forms.Form):
		community = forms.ModelChoiceField(queryset=Community.objects.all(), initial=community_id)
		note = forms.CharField(widget=forms.Textarea)
	f = queue_add_form()
	if request.user.is_authenticated():
    # Do something for authenticated users.
		a = "Welcome %s" % request.user.last_name
		a += "Log out"
	else:
		a = AuthenticationForm()
    # Do something for anonymous users.
	l = reverse(Parking.views.queue_add)
	s = 'Register'
	r = reverse('Parking.views.reservation_list', args=[c.id])
	q = reverse('Parking.views.queue_list', args=[c.id])
 	return render_to_response('Common/community_detail.html',
							  {
								'community':c,
								'account':a,
								'form':f,
								'action':l,
								'submit':s,
								'reservation':r,
								'queue':q,
								},
                              context_instance=RequestContext(request),
							  )


@login_required(login_url='/reservation/login/')
def account(request, user_id):
	return render_to_response('Common/profile.html')

@login_required(login_url='/reservation/login/')
def profile(request):
	user_id = request.user.user_id
	return account(request, user_id)

def logout(request, next):
	logout(request)
	if True:
		#if anonymous can view previous page
		HttpResponseRedirect(next)
	else:
		#else redirect to main page
		HttpResponseRedirect(next)
    # Redirect to a success page.

@login_required(login_url='/reservation/login/')
def index(request):
	return render_to_response('Common/index.html')
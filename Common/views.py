# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
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


@login_required(login_url='/reservation/login/')
def community_list(request, page):
	# pagination later
	community_list = Community.objects.all().order_by('address')
	return render_to_response('Common/community_list.html', {'community_list': community_list },
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def community_detail(request, community_id):
	class queue_add_form(forms.Form):
		community = forms.ModelChoiceField(queryset=Community.objects.all(), initial=community_id)
		note = forms.CharField(widget=forms.Textarea)
	if request.method != 'POST':
		c = get_object_or_404(Community, pk=community_id)
		f = queue_add_form()
		# Do something for anonymous users.
		#l = reverse(Parking.views.queue_add)
		s = 'Register'
		r = reverse('Parking.views.reservation_list', args=[c.id])
		q = reverse('Parking.views.queue_list', args=[c.id])
		return render_to_response('Common/community_detail.html',
								  {
									'community':c,
									'form':f,
									'submit':s,
									'reservation':r,
									'queue':q,
									},
								  context_instance=RequestContext(request),
								  )

	# if it is 'POST'
	else:
		# then, bound the request into defined form
		f = queue_add_form(request.POST)
		# if the requested form is valid
		if f.is_valid():
			# then, add the request into database
			q = Parking.models.Queue()
			Parking.models.Queue.objects.get_or_create(
				user_id=request.user.id,
				community_id=f.cleaned_data['community'],
				note = f.cleaned_data['note'],
			)
			return HttpResponseRedirect(q.link())
			'''
			q.objects.get(user_id=request.user.id, community_id=f.cleaned_data['community'])
			if q is not None:
				# what user id?
				q.user_id = request.user.id
				q.community = f.cleaned_data['community']
				q.note = f.cleaned_data['note']
				# remember to save it!
				q.save()
				# and then redirect the browser to the queue_detail, q.link is defined in model
				return HttpResponseRedirect(q.link())
			else:
				return HttpResponse("already")
				'''
		else:
			# push error message to message mechanism
			# set initial value for valid value
			# abd redirect to the forms, for the user to refill
			return HttpResponseRedirect(q.link())
	#

@login_required(login_url='/reservation/login/')
def account(request, user_id):
	return render_to_response('Common/account.html',
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def profile(request):
	user_id = request.user.id
	return render_to_response('Common/profile.html',
								context_instance=RequestContext(request),)

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
	return render_to_response('Common/index.html',
								context_instance=RequestContext(request),)


def reserved(request, community_id):
	return render_to_response('Common/reserved.html',
								context_instance=RequestContext(request),)
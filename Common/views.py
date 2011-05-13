# Create your views here.
import Queue
import django
from django.conf import settings
from django.core.mail import send_mass_mail
from django.core.paginator import Paginator, EmptyPage
from django.forms.widgets import RadioSelect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms
from django.contrib import auth
# 1. community_list (request, community_id, GET)
#	community_address (list)
# 2. community_detail (request, community_id, GET)
#	link to reservation list (3)
#	link to queue list (4)
#	form to apply for parking queue (send POST request to add_queue (7))
from Common.models import Community, Profile
import Parking
from django.contrib.auth.decorators import login_required, permission_required
from Parking.models import Area
import Sauna


@login_required(login_url='/reservation/login/')
def community_list(request):
	community_list = Community.objects.all()
	paginator = Paginator(community_list, 50) # Show 25 contacts per page
	try:
		page = paginator.page(int(request.GET.get('page')))
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		page = paginator.page(paginator.num_pages)
	except:
		page = paginator.page(1)
	communities = page.object_list

	return render_to_response('Common/community_list.html', {'page': page, 'communities': communities, },
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def community_detail(request, community_id):
	class queue_add_form(forms.Form):
		community = forms.ModelChoiceField(queryset=Community.objects.all(), initial=community_id)
		service = forms.ChoiceField(
			widget=RadioSelect,
			choices=(('s', 'Sauna'),('p', 'Parking'),
    	))
		note = forms.CharField(widget=forms.Textarea)
	if request.method == 'POST':
		# then, bound the request into defined form
		f = queue_add_form(request.POST)
		# if the requested form is valid
		if f.is_valid():
			# then, add the request into database
			if f.cleaned_data['service'] == 'p':
				service = "parking"
				reservedObject = Parking.models.Queue.objects
			else:
				service = "sauna"
				reservedObject = Parking.models.Queue.objects
			reserved, created = reservedObject.get_or_create(
				user_id=request.user.id,
				community_id=f.cleaned_data['community'],
				defaults={'note': f.cleaned_data['note']},
			)
			if created:
				toResident = (
					'Reservation confirmed',
					'Dear %s,\nThis email is to confirm your reservation of %s in community %s. We will contact you when the service is available.\n Best regards,\nSKH Staff' % (request.user.get_full_name, service, Community.objects.get(id=f.cleaned_data['community'])),
					settings.EMAILS['staff'],
					[request.user.email])
				toManager = (
					'New reservation',
					'Dear staff,\nThis email is to inform new reservation of %s in community %s.\n Best regards,\nSKH System' % (service, Community.objects.get(id=f.cleaned_data['community'])),
					settings.EMAILS['system'],
					['staff@skh.fi'])
				send_mass_mail((toResident, toManager), fail_silently=False)
				return HttpResponseRedirect(reverse('Common.views.reserved'))
			else:
				pass
		else:
			pass
	else:
		c = get_object_or_404(Community, pk=community_id)
		f = queue_add_form()
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


@permission_required('Common.view_profile', login_url='/reservation/permissions_warning/')
def account_list(request):
	# pagination later
	accounts = Profile.objects.all().order_by('last_name')
	return render_to_response('Common/account_list.html', {'accounts': accounts},
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def account_detail(request, user_id):
	return render_to_response('Common/account_detail.html',
								context_instance=RequestContext(request),)

'''
@login_required(login_url='/reservation/login/')
def area_list(request, community_id):
	areas = Area.objects.all().order_by('name')
	return render_to_response('Common/area_list.html', {'areas': areas},
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def area_detail(request, community_id):
	return render_to_response('Common/area_detail.html',
								context_instance=RequestContext(request),)
'''
@permission_required('Common.view_queue', login_url='/reservation/login/')
def queue_list(request, community_id):
	queues = Queue.objects.all().order_by('queue.user.last_name')
	return render_to_response('Parking/queue_list.html',{'queues': queues},
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def queue_detail(request, community_id):
	return render_to_response('Common/queue_detail.html',
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def profile(request):
	user_id = request.user.id
	return render_to_response('Common/profile.html',
								context_instance=RequestContext(request),)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/reservation")

@login_required(login_url='/reservation/login/')
def index(request):
	return render_to_response('Common/index.html',
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def reserved(request):
	return render_to_response('Common/reserved.html',
								context_instance=RequestContext(request),)

@login_required(login_url='/reservation/login/')
def permissions_warning(request):
		return render_to_response('Common/permissions_warning.html',
								context_instance=RequestContext(request),)

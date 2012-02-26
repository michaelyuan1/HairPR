from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from users.models import User
from django.core.mail import send_mail


def home(request):
	return render_to_response('users/home.html', context_instance=RequestContext(request))
	
def submitEmail(request):
	newUser = User(email=request.POST['email'])
	newUser.save();
	send_mail('Thanks For Signing Up for HairPR!', 'Thank You!', 'buhbuhbuhbuhbuhbuhbowser@gmail.com', [request.POST['email']], fail_silently=False)
	return render_to_response('users/thankyou.html', context_instance=RequestContext(request))
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from users.models import User

def home(request):
	return render_to_response('users/home.html', context_instance=RequestContext(request))
	
def submitEmail(request):
	newUser = User(email=request.POST['email'])
	return render_to_response('users/thankyou.html', context_instance=RequestContext(request))
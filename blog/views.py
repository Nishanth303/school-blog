from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Post
from django.core.mail import send_mail

# Create your views here.
def home_page(request):
	return render(request, 'blog/home_page.html')


def about(request):
	return render(request, 'blog/about.html')

def event(request):
	return render(request, 'blog/event.html')
	
def calendar(request):
	return render(request, 'blog/calendar.html')

def contact(request):
	return render(request, 'blog/contact.html')

def class_a(request):
	return render(request, 'blog/class_a.html')

def login(request):
	return render(request, 'blog/login.html')

def login_submit(request):
	context = {}

	email = request.POST.get('email','')
	psd = request.POST.get('password', '')

	user = authenticate(username=email, password=psd)
	if user is not None:
		# the password verified for the user
			if user.is_active:
				context['message'] = "User is valid, active and authenticated"
				return render (request,'index.html',context)	
			else:
					context['message']= "The password is valid, but the account has been disabled!"
	else:
		# the authentication system was unable to verify the username and password
			context['message']= "The username and password were incorrect."
	
	return render (request,'login.html',context)

def index (request):
	return render(request, 'blog/index.html')
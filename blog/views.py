from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Post
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import PostForm
from django.shortcuts import redirect

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
				return render (request,'class_info.html',context)	
			else:
					context['message']= "The password is valid, but the account has been disabled!"
	else:
		# the authentication system was unable to verify the username and password
			context['message']= "The username and password were incorrect."
	
	return render (request,'login.html',context)

def class_info (request):
	return render(request, 'blog/class_info.html')

def Ist_std(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			
			
			post.save()
			return redirect('blog/IInd_std.html', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/Ist_std.html')

def IInd_std(request):
	return render(request, 'blog/IInd_std.html', {'form': form})

def IIIrd_std(request):
	return render(request, 'blog/IIIrd_std.html')

def IVth_std(request):
	return render(request, 'blog/IVth_std.html')

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog/home_page.html', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
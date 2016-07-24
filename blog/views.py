from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def home_page(request):
	return render(request, 'blog/home_page.html')


def about(request):
	
	return render(request, 'blog/about.html')
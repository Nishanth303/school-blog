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

p = 0; a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0; h = 0; i = 0;
j = 0; k = 0; l = 0; m = 0; n = 0; o = 0; q = 0;
r = 0; s = 0; t = 0; 
def Ist_std(request):
	global p,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,r,s,t
	my_dictionary = {
		"p" : p, "a" : a, "b" : b, "c" : c, "d" : d, "e" : e, "f" : f,
"g" : g, "h" : h, "i" : i, "j" : j, "k" : k,
		"l" : l, "m" : m, "n" : n, "o" : o, "q" : q, "r" : r, "s" : s, "t" : t, 
	}
	if request.GET.get('add'):
		p = p+1
		my_dictionary["p"] = p
			
	if request.GET.get('add1'):
		a = a+1
		my_dictionary["a"] = a
			
	if request.GET.get('add2'):
		b = b+1
		my_dictionary["b"] = b
			
	if request.GET.get('add3'):
		c = c+1
		my_dictionary["c"] = c
           
	if request.GET.get('add4'):
		d = d+1
		my_dictionary["d"] = d
			
	if request.GET.get('add5'):
		e = e+1
		my_dictionary["e"] = e
			
	if request.GET.get('add6'):
		f = f+1
		my_dictionary["f"] = f
			
	if request.GET.get('add7'):
		g = g+1
		my_dictionary["g"] = g
			
	if request.GET.get('add8'):
		h = h+1
		my_dictionary["h"] = h
			
	if request.GET.get('add9'):
		i = i+1
		my_dictionary ["i"] = i

	if request.GET.get('add10'):
		j = j+1
		my_dictionary ["j"] = j

	if request.GET.get('add11'):
		k = k+1
		my_dictionary["k"] = k

	if request.GET.get('add12'):
		l = l+1
		my_dictionary["l"] = l

	if request.GET.get('add13'):
		m = m+1
		my_dictionary["m"] = m

	if request.GET.get('add14'):
		n = n+1
		my_dictionary["n"] = n

	if request.GET.get('add15'):
		o = o+1
		my_dictionary["o"] = o

	if request.GET.get('add16'):
		q = q+1
		my_dictionary["q"] = q

	if request.GET.get('add17'):
		r = r+1
		my_dictionary ["r"] = r

	if request.GET.get('add18'):
		s = s+1
		my_dictionary ["s"] = s

	if request.GET.get('add19'):
		t = t+1
		my_dictionary ["t"] = t

	return render(request, "blog/Ist_std.html", my_dictionary)

u=0; v=0
def IInd_std(request):

	global u,v
	my_dictionary = {
		"u" : u, "v" : v
	}
	if request.GET.get('add20'):
		u = u+1
		my_dictionary["u"] = u
			
	

	if request.GET.get('add21'):
		v = v+1
		my_dictionary["v"] = v
			
		


	return render(request, 'blog/IInd_std.html',my_dictionary)

ba=0; bb=0; bc=0; bd=0; be=0; bf=0; bg=0; bh=0; bi=0; bj=0; bk=0; bl=0; bm=0; bn=0; bo=0;
bp=0; bq=0; br=0; bs=0; bt=0
def IIIrd_std(request):

	global ba,bb,bc,bd,be,bf,bg,bh,bi,bj,bk,bl,bm,bn,bo,bp,bq,br,bs,bt
	my_dictionary = {
		"ba" : ba, "bb" : bb, "bc" : bc,
		"bd" : bd, "be" : be, "bf" : bf, "bg" : bg, "bh" : bh, "bi" : bi, "bj" : bj, "bk" : bk, 
		"bl" : bl, "bm" : bm, "bn" : bn, "bo" : bo, "bp" :bp, 
		"bq" : bq, "br" : br, "br" : br, "bs" : bs, "bt" : bt
	}

	if request.GET.get('add40'):
		ba = ba+1
		my_dictionary["ba"] = ba


	if request.GET.get('add41'):
		bb = bb+1
		my_dictionary["bb"] = bb

	if request.GET.get('add42'):
		bc = bc+1
		my_dictionary["bc"] = bc

	if request.GET.get('add43'):
		bd = bd+1
		my_dictionary["bd"] = bd

	if request.GET.get('add44'):
		be = be+1
		my_dictionary["be"] = be

	if request.GET.get('add45'):
		bf = bf+1
		my_dictionary["bf"] = bf

	if request.GET.get('add46'):
		bg = bg+1
		my_dictionary["bg"] = bg

	if request.GET.get('add47'):
		bh = bh+1
		my_dictionary["bh"] = bh

	if request.GET.get('add48'):
		bi = bi+1
		my_dictionary["bi"] = bi

	if request.GET.get('add49'):
		bj = bj+1
		my_dictionary["bj"] = bj

	if request.GET.get('add50'):
		bk = bk+1
		my_dictionary["bk"] = bk

	if request.GET.get('add51'):
		bl = bl+1
		my_dictionary["bl"] = bl

	if request.GET.get('add52'):
		bm = bm+1
		my_dictionary["bm"] = bm

	if request.GET.get('add53'):
		bn = bn+1
		my_dictionary["bn"] = bn	

	if request.GET.get('add54'):
		bo = bo+1
		my_dictionary["bo"] = bo

	if request.GET.get('add55'):
		bp = bp+1
		my_dictionary["bp"] = bp

	if request.GET.get('add56'):
		bq = bq+1
		my_dictionary["bq"] = bq

	if request.GET.get('add57'):
		br = br+1
		my_dictionary["br"] = br

	if request.GET.get('add58'):
		bs = bs+1
		my_dictionary["bs"] = bs

	if request.GET.get('add59'):
		bt = bt+1
		my_dictionary["bt"] = bt	

	return render(request, 'blog/IIIrd_std.html',my_dictionary)

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



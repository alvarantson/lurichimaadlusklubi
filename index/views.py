from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import Lang, Contact, Navbar_lang, Social_media, Toetaja
from .models import Index_lang
from blog.models import Post
from pood.models import Toode
# Create your views here.
def index(request):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'

	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/') #INDEX\i puhul '/'
	

	return render(request, 'index.html', context={
		'contact':Contact.objects.all()[0],
		'navbar_lang':Navbar_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'flags': Lang.objects.all(),
		'lang':Index_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'social_media': Social_media.objects.all(),
		'toetajad': Toetaja.objects.all(),
		'news': Post.objects.all().order_by("-date")[:3],
		'merch': Toode.objects.filter(lang=Lang.objects.get(lang=request.session['lang']))[:3]
		})
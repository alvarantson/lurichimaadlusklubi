from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import Lang, Contact, Navbar_lang, Social_media, Toetaja
from .models import Pood_lang, Toode, Toode_lang
# Create your views here.
def pood(request):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'

	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/pood') #INDEX\i puhul '/'
	

	return render(request, 'pood.html', context={
		'contact':Contact.objects.all()[0],
		'navbar_lang':Navbar_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'flags': Lang.objects.all(),
		'lang':Pood_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'social_media': Social_media.objects.all(),
		'toetajad': Toetaja.objects.all(),
		'tooted': Toode.objects.filter(lang=Lang.objects.get(lang=request.session['lang']))
		})

def toode(request, toode_id):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'

	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/toode/'+str(toode_id)+"/") #INDEX\i puhul '/'
	

	return render(request, 'toode.html', context={
		'contact':Contact.objects.all()[0],
		'navbar_lang':Navbar_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'flags': Lang.objects.all(),
		'lang':Toode_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'social_media': Social_media.objects.all(),
		'toetajad': Toetaja.objects.all(),
		'toode': Toode.objects.get(id = toode_id)
		})
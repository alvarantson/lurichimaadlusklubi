from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import Lang, Contact, Navbar_lang, Social_media, Toetaja
from .models import Hinnakiri_lang
# Create your views here.
def hinnakiri(request):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'

	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/hinnakiri') #INDEX\i puhul '/'
	

	return render(request, 'hinnakiri.html', context={
		'contact':Contact.objects.all()[0],
		'navbar_lang':Navbar_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'flags': Lang.objects.all(),
		'lang':Hinnakiri_lang.objects.get(lang=Lang.objects.get(lang=request.session['lang'])),
		'social_media': Social_media.objects.all(),
		'toetajad': Toetaja.objects.all()
		})
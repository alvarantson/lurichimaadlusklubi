from django.contrib import admin
from navbar.models import Lang, Contact, Navbar_lang, Social_media, Toetaja

# Register your models here.
admin.site.register(Contact)
admin.site.register(Navbar_lang)
admin.site.register(Lang)
admin.site.register(Social_media)
admin.site.register(Toetaja)
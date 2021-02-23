from django.db import models

# Create your models here.
class Lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	flag = models.ImageField()
	def __str__(self):
		return self.lang

class Contact(models.Model):
	name = models.CharField(max_length=30, unique=True)
	phone = models.CharField(max_length=15, unique=True)
	email = models.CharField(max_length=50, unique=True)
	address = models.CharField(max_length=999, unique=True)
	gmaps_x = models.CharField(max_length=10, unique=True)
	gmaps_y = models.CharField(max_length=10, unique=True)
	gmaps_zoom = models.CharField(max_length=2, unique=True)
	gmaps_API = models.CharField(max_length=64, unique=True)
	open_hours = models.CharField(max_length=64, unique=True, blank=True)
	footer_info = models.TextField(blank=True)
	SEO_tags = models.TextField(blank=True)
	SEO_description = models.TextField(blank=True)
	SEO_author = models.CharField(max_length=999, blank=True)
	def __str__(self):
		return 'Dont create a new entry! Ara tee uut sissekannet!'

class Navbar_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	index = models.CharField(max_length=15, blank=True)
	hinnakiri = models.CharField(max_length=15, blank=True)
	meist = models.CharField(max_length=15, blank=True)
	pood = models.CharField(max_length=15, blank=True)
	treenerid = models.CharField(max_length=15, blank=True)
	tutvustus = models.CharField(max_length=15, blank=True)
	blog = models.CharField(max_length=15, blank=True)
	footer_info = models.TextField(blank=True)
	logo = models.ImageField()
	def __str__(self):
		return self.lang.lang


class Social_media(models.Model):
	url = models.CharField(max_length=999, blank=True)
	icon = models.CharField(max_length=20, blank=True)
	def __str__(self):
		return self.url + ' - ' + self.icon

class Toetaja(models.Model):
	url = models.CharField(max_length=999, blank=True)
	logo = models.ImageField(blank=True)
	def __str__(self):
		return self.url
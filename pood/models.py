from django.db import models
from navbar.models import Lang
# Create your models here.

class Pood_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)
	title = models.CharField(max_length=999, blank=True)


	def __str__(self):
		return self.lang.lang

class Toode_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)
	disclaimer = models.TextField(blank=True)
	tagasi = models.CharField(max_length=999, blank=True)


	def __str__(self):
		return self.lang.lang

class Toode(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	nimi = models.CharField(max_length=999, blank=True)
	hind = models.FloatField(blank=True)
	kirjeldus = models.TextField(blank=True)
	pilt = models.ImageField(blank=True)
	pilt2 = models.ImageField(blank=True)
	pilt3 = models.ImageField(blank=True)
	pilt4 = models.ImageField(blank=True)

	def __str__(self):
		return self.lang.lang + " - " + self.nimi + ": " + str(self.hind) + "€"
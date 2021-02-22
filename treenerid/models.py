from django.db import models
from navbar.models import Lang
# Create your models here.
class Treenerid_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)
	title = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.lang.lang

class Treener(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	nimi = models.CharField(max_length=999)
	phone = models.CharField(max_length=999, blank=True)
	email = models.CharField(max_length=999, blank=True)
	kirjeldus = models.TextField(blank=True)
	pilt = models.ImageField(blank=True)

	def __str__(self):
		return self.lang.lang + " - " + self.nimi
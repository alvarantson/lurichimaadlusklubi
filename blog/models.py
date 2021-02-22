from django.db import models
from navbar.models import Lang
# Create your models here.
class Blog_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)
	title = models.CharField(max_length=999, blank=True)
	tagasi = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.lang.lang

class Post(models.Model):
	tiitel = models.CharField(max_length=999, blank=True)
	pilt = models.ImageField(blank=True)
	sisu = models.TextField(blank=True)
	date = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.tiitel + " - " + str(self.date)
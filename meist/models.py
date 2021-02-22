from django.db import models
from navbar.models import Lang
# Create your models here.
class Meist_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)
	
	def __str__(self):
		return self.lang.lang
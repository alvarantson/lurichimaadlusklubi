from django.db import models
from navbar.models import Lang
# Create your models here.
class Hinnakiri_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)
	title = models.CharField(max_length=999, blank=True)
	text = models.TextField(blank=True)
	title2 = models.CharField(max_length=999, blank=True)
	pricing = models.TextField(blank=True)
	
	def __str__(self):
		return self.lang.lang

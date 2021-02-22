from django.db import models
from navbar.models import Lang
# Create your models here.
class Index_lang(models.Model):
	lang = models.OneToOneField(Lang, on_delete=models.CASCADE)
	bg = models.ImageField(blank=True)

	liitu_meiega = models.CharField(max_length=999, blank=True)
	lurchist = models.CharField(max_length=999, blank=True)
	meist = models.CharField(max_length=999, blank=True)
	
	def __str__(self):
		return self.lang.lang

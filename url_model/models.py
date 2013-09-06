from django.db import models

# Create your models here.

class Meta_info(models.Model):
	url=models.CharField(max_length=120)
	title=models.CharField(max_length=120)
	meta=models.CharField(max_length=500)


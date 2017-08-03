from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=9, default="")
	rank = models.IntegerField(default = 1)
	nickname =models.CharField(max_length=9, default="")
	url = models.TextField(validators=[URLValidator()], default="")
	
	def __str__(self):
		return self.name
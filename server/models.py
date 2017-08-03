from django.db import models

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=9, default="강다니엘")
	rank = models.IntegerField(default = 1)
	position = models.CharField(max_length=60, default="센터")
	
	
	def __str__(self):
		return self.name
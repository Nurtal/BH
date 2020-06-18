from django.db import models
from jsonfield import JSONField


class Ingredient(models.Model):
	"""
	"""
	
	## attribute
	name = models.TextField(default="NA")
	
	
	

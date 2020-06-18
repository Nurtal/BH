from django.db import models
from jsonfield import JSONField


class Receipe(models.Model):
	"""
	name : name of the receipe
	receipe_type : entre/main/dessert
	instruction : how to prepare the receipe
	ingredient_list : what you need to perform the receipe
	"""
	
	## attribute
	name = models.TextField(default="NA")
	receipe_type = models.TextField(default="NA")
	instruction = models.TextField(default="NA")
	ingredient_list = JSONField()
	
	
	

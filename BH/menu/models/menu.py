from django.db import models
from jsonfield import JSONField


class Menu(models.Model):
	"""
	name : the name of the menu
	entre_name = name of the receipe for entre
	main_name = name of the receipe for main
	dessert_name = name of the receipe for dessert
	
	"""
	
	## attribute
	name = models.TextField(default="NA")
	entre_name = models.TextField(default="NA")
	main_name = models.TextField(default="NA")
	dessert_name = models.TextField(default="NA")

	
	
	def generate_random_menu(self):
		"""
		"""
		
		## importation
		
		## select all entre receipe
		
		## pick random entre
		
		## update entre attribute
	
	
	
	def get_random_entre(self):
		"""
		"""
		
		## importation
		
		## select all main receipe
		
		## pick random main
		
		## update main attribute
	
	
	
	def get_random_dessert(self):
		"""
		"""
		
		## importation
		
		## select all dessert receipe
		
		## pick random dessert
		
		## update dessert attribute

	

	def get_ingredient_list(self):
		"""
		"""
		
		## importation
		
		## extract ingredients from entre
		
		## extract ingredients from main
		
		## extract ingredients from dessert
		
		## return list of ingredients


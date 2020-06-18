from django.db import models
from jsonfield import JSONField


class WeekMenu(models.Model):
	"""
	"""
	
	## attribute
	monday_rep1 = models.TextField(default="NA")
	monday_rep2 = models.TextField(default="NA")
	lock_mrep1 = models.BooleanField(default=False)
	lock_mrep2 = models.BooleanField(default=False)
	
	tuesday_rep1 = models.TextField(default="NA")
	tuesday_rep2 = models.TextField(default="NA")
	lock_trep1 = models.BooleanField(default=False)
	lock_trep2 = models.BooleanField(default=False)
	
	wednesday_rep1 = models.TextField(default="NA")
	wednesday_rep2 = models.TextField(default="NA")
	lock_wrep1 = models.BooleanField(default=False)
	lock_wrep2 = models.BooleanField(default=False)
	
	thirsday_rep1 = models.TextField(default="NA")
	thirsday_rep2 = models.TextField(default="NA")
	lock_threp1 = models.BooleanField(default=False)
	lock_threp2 = models.BooleanField(default=False)
	
	friday_rep1 = models.TextField(default="NA")
	friday_rep2 = models.TextField(default="NA")
	lock_frep1 = models.BooleanField(default=False)
	lock_frep2 = models.BooleanField(default=False)
	
	
	saturday_rep1 = models.TextField(default="NA")
	saturday_rep2 = models.TextField(default="NA")
	lock_srep1 = models.BooleanField(default=False)
	lock_srep2 = models.BooleanField(default=False)
	
	sunday_rep1 = models.TextField(default="NA")
	sunday_rep2 = models.TextField(default="NA")
	lock_sunrep1 = models.BooleanField(default=False)
	lock_sunrep2 = models.BooleanField(default=False)
	
	
	def generate_random_week(self):
		"""
		"""
	
	
	def update_random_week(self):
		"""
		"""
		
		## update monday rep 1 if not lock
		
		## update monday rep 2 if not lock
		
		## update tuesday rep 1 if not lock
		
		## update tuesday rep 2 if not lock
		
		## update wednesday rep 1 if not lock
		
		## update wednesday rep 2 if not lock
		
		## update tuesday rep 1 if not lock
		
		## update tuesday rep 2 if not lock
		
		## update friday rep 1 if not lock
		
		## update friday rep 2 if not lock
		
		## update saturday rep 1 if not lock
		
		## update saturday rep 2 if not lock
		
		## update sunday rep 1 if not lock
		
		## update sunday rep 2 if not lock

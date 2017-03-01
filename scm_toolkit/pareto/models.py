from django.db import models
from crum import get_current_user

	
class abc_multiloc(models.Model):
	item_id = models.CharField(max_length=15)
	item_desc = models.CharField(max_length=80,blank=True, default=None)
	loc_id = models.CharField(max_length=15)
	loc_desc = models.CharField(max_length=50,blank=True, default=None)
	loc_type = models.CharField(max_length=20,blank=True, default=None)
	sales = models.FloatField(null=True, blank=True, default=None)
	creator = models.CharField(max_length=20, default=None)
	last_editor = models.CharField(max_length=20, default=None)
							
			
		
	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.creator = user
		self.last_editor = user
		super(abc_multiloc, self).save(*args, **kwargs)



class abc_multiloc_analysis(models.Model):
	item_id = models.CharField(max_length=15)
	item_desc = models.CharField(max_length=80,blank=True, default=None)
	loc_id = models.CharField(max_length=15)
	loc_desc = models.CharField(max_length=50,blank=True, default=None)
	loc_type = models.CharField(max_length=20,blank=True, default=None)
	sales = models.FloatField(null=True, blank=True, default=None)
	cum_sum = models.FloatField(null=True, blank=True, default=None)
	ABC_Class = models.CharField(max_length=1, null=True, blank=True, default=None)
	creator = models.CharField(max_length=20, default=None)
	last_editor = models.CharField(max_length=20, default=None)
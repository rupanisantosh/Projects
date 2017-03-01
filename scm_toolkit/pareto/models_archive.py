from django.db import models


class abc_multi_loc(models.Model):
	user_id = models.CharField(max_length=15,default='1', editable=False)
	Item_id = models.CharField(max_length=15)
	item_desc = models.CharField(max_length=80)
	loc_id = models.CharField(max_length=15)
	loc_desc = models.CharField(max_length=50)
	loc_type = models.CharField(max_length=20)
	sales = models.FloatField(null=True, blank=True, default=None)
							
	
	def __str__(self):
		return self.user_id

		
		##################
		
			def save(self, *args, **kwargs):
		user = get_current_user()
		if not self.pk:
			self.creator = user
		else:
			self.last_editor = user
		super(abc_multiloc, self).save(*args, **kwargs)
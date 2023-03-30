from django.db import models
from profiles.models import User

# Create your models here.
class CaloEachDay(models.Model):
	user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	calo_in = models.FloatField()
	calo_out = models.FloatField()
	date_time_save = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.date_time_save)

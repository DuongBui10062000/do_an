from django.db import models

# Create your models here.
class NameOfFood(models.Model):
	name_food = models.CharField(max_length=100)
	unit = models.IntegerField()
	calo = models.IntegerField()

class ARM(models.Model):
	EI = (
			('Ít vận động( ít hoặc không tập thể dục)', 'Ít vận động( ít hoặc không tập thể dục)'),
			('Vận động cường độ cao', 'Vận động cường độ cao'),
			('Vận động nhẹ( tập thể dục 1-3 ngày/tuần)', 'Vận động nhẹ( tập thể dục 1-3 ngày/tuần)'),
			('Vận động vừa phải( Tập thể dục 3-5 ngày/tuần)', 'Vận động vừa phải( Tập thể dục 3-5 ngày/tuần)'),
			('Vận động nhiều( tập thể dục 6-7 ngày/tuần)', 'Vận động nhiều( tập thể dục 6-7 ngày/tuần)'),
		)
	exertion_intensity = models.CharField(max_length=100, null=True, choices=EI)
	ARM_factor = models.FloatField()
	def __str__(self):
		return self.exertion_intensity
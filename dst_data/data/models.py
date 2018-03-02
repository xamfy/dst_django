from django.db import models

class Data(models.Model):
	date = models.DateField()
	time = models.TimeField()
	doy = models.IntegerField()
	dst = models.IntegerField()

	def __str__(self):
		# return self.date
		return '%s/%s/%s -%s hour' % (self.date.year, self.date.month, self.date.day,
			self.time.hour)
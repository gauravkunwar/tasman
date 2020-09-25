from django.db import models

# Create your models here.
class Data (models.Model):
	salinity = models.DecimalField(max_digits=8,decimal_places=3)
	conductivity = models.DecimalField(max_digits=8,decimal_places=3)
	temperature	= models.DecimalField(max_digits=8,decimal_places=3)
	depth = models.DecimalField(max_digits=8,decimal_places=3)

	def __str__(self):
	 	return '%d m depth' % (self.depth)

class Technology (models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name or ''

class Freq (models.Model):
	tech = models.ForeignKey(Technology, on_delete=models.CASCADE)
	frequency = models.DecimalField(max_digits=8,decimal_places=3)
	attenuation = models.DecimalField(max_digits=8,decimal_places=5)

	def __str__(self):
		return '%s %d' % (self.tech, self.frequency)


from django.db import models

# Create your models here.

# A model tells Django how to work with the data
# that will be stored in the app.  Code-wise, a model is
# just a class

class Topic(models.Model):
	"""A topic the user is learning about."""
	text = models.CharField(max_length = 200)
	data_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text



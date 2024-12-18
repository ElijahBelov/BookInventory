from django.db import models

# Create your models here.
class Book(models.Model):
	entry_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	pub_date = models.DateField()
	isbn = models.CharField(max_length=17)

	def __str__(self):
		return self.title


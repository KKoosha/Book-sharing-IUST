from django.db import models

# Create your models here.
class Books(models.Model):

	name = models.CharField(max_length = 30)       #name of book
	author = models.CharField(max_length = 30)     #author of book	
	uploader = models.CharField(max_length = 30)
	email = models.EmailField(blank = True, verbose_name = 'e-mail')
	upload_date = models.DateField()
	rate = models.CharField(max_length = 1)
	comment = models.CharField(max_length = 200)
	url_pdf = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name
from django.db import models

class Books(models.Model):

	name = models.CharField(max_length = 30)       #name of book
	author = models.CharField(max_length = 30)     #author of book	
	uploader = models.CharField(max_length = 30)
	email = models.EmailField(blank = True, verbose_name = 'e-mail')
	upload_date = models.DateField()
	

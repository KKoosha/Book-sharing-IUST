from django.db import models

# Create your models here.
class PDF(models.Model):
    docfile = models.FileField(upload_to='PDF')
    name=models.CharField(max_length='100')
    author=models.CharField(max_length='100')
    comment=models.CharField(max_length='300')
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    
    # Other fields here
    
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Dragons.")
    
    def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)
			
		post_save.connect(create_user_profile, sender=User)

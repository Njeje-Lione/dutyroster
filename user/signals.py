#Signals in Django are a mechanism for decoupling various components of an application.
# They allow certain pieces of code to be executed when particular events occur.
#These events can be anything from a user logging in to a new record being added to a database.
#for our case it works so that if a user is created we dont need to create a profile the profile is create automatically for us.
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(staff=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
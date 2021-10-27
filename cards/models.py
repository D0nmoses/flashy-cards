from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    '''	
    Class to define a user's profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    profile_pic = models.ImageField(upload_to="profile-pic/", blank=True, default='/profile-pic/default-no-profile-pic.jpg')

    def __str__(self):

        return self.user.username

    @classmethod
    def get_profiles(cls):

        profiles = Profile.objects.all()

        return profiles

    @classmethod
    def get_other_profiles(cls,user_id):


        profiles = Profile.objects.all()

        other_profiles = []

        for profile in profiles:

            if profile.user.id != user_id:

                other_profiles.append(profile)

        return other_profiles


# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Subject(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Card(models.Model):

    title = models.CharField(max_length=20)
    notes = models.TextField(max_length= 100)
    dateAdded = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:

        ordering = ['-dateAdded']

    def save_card(self):

        self.save()

    @classmethod
    def get_cards(cls):

        cards = Card.objects.all()

        return cards

    @classmethod
    def get_profile_cards(cls, profile_id):

        profile_cards = Card.objects.filter(profile=profile_id).all()

        return profile_cards


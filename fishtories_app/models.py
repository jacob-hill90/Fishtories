from django.db import models
from django.contrib.auth.models import AbstractUser

def fish_upload_path(instance, filename):
    return '/'.join(['fish_picture', str(instance.owner), filename])

def profile_upload_path(instance, filename):
    return '/'.join(['profile_picture', str(instance.username), filename])

class AppUser(AbstractUser):
    zipcode = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    is_active_catches = models.BooleanField(default=True)
    def __str__(self):
        return self.username

class CatchData(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date = models.DateField()
    season = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.FloatField()
    depth = models.PositiveIntegerField(null=True)
    fishing_method = models.CharField(max_length=50)
    length = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    catch_picture = models.ImageField(upload_to='catch_pics/', blank=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.owner.username}'s {self.species} catch on {self.date}"

class FishDB(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    fish_record = models.CharField(max_length=100, null=True)
    fish_docs = models.TextField()
    fish_pic = models.CharField(max_length=100)
        
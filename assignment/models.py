from django.db import models

# Create your models here.

class Team (models.Model):
    full_name = models.CharField(max_length=50,)
    position = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    profile = models.FileField(upload_to='teams/,')
    twitter_url = models.CharField(max_length=78, blank=True)
    instagram_url = models.CharField(max_length=78, blank=True)
    facebook_url = models.CharField(max_length=78,blank=True)
    linkedin_url = models.CharField(max_length=78, blank=True)


class Testimonials(models.Model):
    full_name = models.CharField(max_length=45)
    tittle = models.CharField(max_length=60)
    rating = models.CharField(max_length=50)
    content = models.CharField(max_length=50)


    def _str_(self):
        return f"{self.full_name}  {self.position}"
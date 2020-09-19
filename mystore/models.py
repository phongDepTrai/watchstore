from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=264,unique=True)
    name = models.CharField(max_length=264)   
    brand = models.CharField(max_length=264)
    country = models.CharField(max_length=264)
    chain = models.CharField(max_length=264)
    category = models.CharField(max_length=264)
    sex = models.IntegerField()
    fee = models.IntegerField()
    description = models.TextField()
    state = models.CharField(max_length=264,default="None")
    created = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = "images/")
    def __str__(self):
        return str(self.name)
#Tao class UserProfileInfor
class UserProfileInfo(models.Model):
    #create relationship from this class to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #add any more attribute you want
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to = "users/", blank=True)
    def __str__(self):
        return self.user.username
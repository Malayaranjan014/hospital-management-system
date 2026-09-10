from django.db import models
from django.contrib.auth.models import AbstractUser  #create a custom user model 

# Create your models here.


class User(AbstractUser):
    email=models.EmailField(unique=True)  #to make email unique for each user
    username=models.CharField(max_length=100, null=True, blank=True)  #to make username unique for each user


    USERNAME_FIELD="email"     
    REQUIRED_FIELDS=["username"]  #this is required when we create superuser using email as username field


    def __str__(self):
        return self.username   # Return the username when the object is printed

    def save(self,*args,**kwargs):
        email_username=self.email.split("@")[0]

        if not self.username:
            self.username=email_username
        super(User,self).save(*args,**kwargs)   
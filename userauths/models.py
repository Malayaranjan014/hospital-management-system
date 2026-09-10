from django.db import models
from django.contrib.auth.models import AbstractUser  #create a custom user model 

# Create your models here.


#creting the user type choice doctor or patient
USER_TYPE_CHOICES=(
        ("Doctor","Doctor"),
        ("Patient","Patient"),
    ) 


class User(AbstractUser):
    email=models.EmailField(unique=True)  #to make email unique for each user
    username=models.CharField(max_length=100, null=True, blank=True)  #to make username unique for each user
    user_type=models.CharField(max_length=10,choices=USER_TYPE_CHOICES,null=True,blank=True,default="None")  #to make user type choice doctor or patient



  


    USERNAME_FIELD="email"     
    REQUIRED_FIELDS=["username"]  #this is required when we create superuser using email as username field


    def __str__(self):
        return self.username   # Return the username when the object is printed

    def save(self,*args,**kwargs):
        email_username=self.email.split("@")[0]

        if not self.username:
            self.username=email_username
        super(User,self).save(*args,**kwargs)   
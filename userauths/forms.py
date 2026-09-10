from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User 



#create a form for user registration
class UserRegisterForm(UserCreationForm):
    full_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Name"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Your Password"})) 


    class Meta:
        model=User
        fields=["full_name","email","password1","password2" ,"user_type"]

#create a form for user login
class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Email"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))


    class Meta:
        model=User
        fields=["email","password"]

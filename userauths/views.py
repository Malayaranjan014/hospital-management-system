from django.shortcuts import render,redirect
from django.contrib import messages
from userauths import forms as userauths_forms
from django.contrib.auth import authenticate,login,logout
from doctor import models as doctor_models 
from patient import models as patient_models
from userauths.models import models as userauths_models

# Create your views here.


#create a view for user registration
def register_view(request):
    # if request.user.is_authenticated:
    #     messages.success(request, "You are already logged in.")
    #     return redirect("/")


    #create a form instance and check if the form is valid
    if request.method=="POST":
        form=userauths_forms.UserRegisterForm(request.POST or None)

        #check if the form is valid
        if form.is_valid():
            user=form.save()
            # Get the cleaned data
            full_name=form.cleaned_data.get("full_name")
            email=form.cleaned_data.get("email")
            password1=form.cleaned_data.get("password")
            user_type=form.cleaned_data.get("user_type")

            # Authenticate the user if the form is valid
            user_auth=authenticate(request,email=email,password=password1)

            if user_auth is not None:
                login(request,user_auth)

                if user_type=="Doctor":
                    doctor_models.Doctor.objects.create(user=user,full_name=full_name)
                else :
                    patient_models.Patient.objects.create(user=user,full_name=full_name,email=email)

                messages.success(request, f"Account created successfully for {full_name}. You are now logged in.")
                return redirect("/")

            else:
                messages.error(request, "Authentication failed. Please Try Again.")
                return redirect("userauths:register") 
    else :
        form=userauths_forms.UserRegisterForm()

        context={"form":form}

    return render(request,"userauths/signup.html",context)



#create a view for user login
def login_view(request):
    # if request.user.is_authenticated:
    #     messages.success(request, "You are already logged in.")
    #     return redirect("/")

    if request.method=="POST":
        form=userauths_forms.LoginForm(request.POST or None)

        if form.is_valid():
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")


                #
            try:
                user_instance=userauths_models.User.objects.get(email=email,is_active=True)
                user_authenticate=authenticate(request,email=email,password=password)

                if user_instance is not None :
                    login(request,user_authenticate)
                    messages.success(request, f"Welcome back {user_instance.username}. You are now logged in.")
                    next_url=request.GET.get("next","/")
                    return redirect(next_url)
                else:
                    messages.error(request, "Invalid username or password. Please try again.")
                    

            except:
                messages.error(request, "username or password doesn't exist. Please try again.")
    else:
        form=userauths_forms.LoginForm()

    context={"form":form}
    
    return render(request,"userauths/signin.html",context)


# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logout successful")
#     return redirect("userauths/signout.html")

def logout_view(request):
    logout(request)

    messages.success(request, "Logout successful")

    return render(request, "userauths/signout.html")
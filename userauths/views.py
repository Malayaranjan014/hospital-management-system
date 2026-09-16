from django.shortcuts import render,redirect
from django.contrib import messages
from userauths import forms as userauths_forms
from django.contrib.auth import authenticate,login,logout
from doctor import models as doctor_models 
from patient import models as patient_models
from userauths import models as userauths_models

# Create your views here.
def register_view(request):

    if request.user.is_authenticated:
        messages.success(request, "You are already logged in.")
        return redirect("/")

    if request.method == "POST":

        form = userauths_forms.UserRegisterForm(request.POST)

        if form.is_valid():

            full_name = form.cleaned_data.get("full_name")
            email = form.cleaned_data.get("email")
            user_type = form.cleaned_data.get("user_type")

            # Create user without saving first
            user = form.save(commit=False)

            # Store Doctor/Patient in User model
            user.user_type = user_type

            user.save()

            # Create Doctor or Patient profile
            if user_type == "Doctor":

                doctor_models.Doctor.objects.create(
                    user=user,
                    full_name=full_name
                )

            elif user_type == "Patient":

                patient_models.Patient.objects.create(
                    user=user,
                    full_name=full_name,
                    email=email
                )

            messages.success(
                request,
                f"Account created successfully for {full_name}. Please sign in."
            )

            # Redirect  signin URL
            return redirect("userauths:signin")

        else:

            messages.error(
                request,
                "Please correct the errors below.")

    else:

        form = userauths_forms.UserRegisterForm()

  
    context = {
        "form": form
    }

    return render(
        request,
        "userauths/signup.html",
        context
    )




# login view 
def login_view(request):

    if request.user.is_authenticated:
        messages.success(request, "You are already logged in.")
        return redirect("/")

    if request.method == "POST":

        form = userauths_forms.LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:

                user_instance = userauths_models.User.objects.get(
                    email=email,
                    is_active=True
                )

                user_authenticate = authenticate(
                    request,
                    email=email,
                    password=password
                )

                if user_authenticate is not None:

                    login(request, user_authenticate)

                    messages.success(
                        request,
                        f"Welcome back {user_instance.username}. You are now logged in."
                    )

                    next_url = request.GET.get("next", "/")

                    return redirect(next_url)

                else:

                    messages.error(
                        request,
                        "Invalid email or password. Please try again."
                    )

            except userauths_models.User.DoesNotExist:

                messages.error(
                    request,
                    "Email or password doesn't exist. Please try again."
                )

    else:

        form = userauths_forms.LoginForm()

    context = {
        "form": form
    }

    return render(
        request,
        "userauths/signin.html",
        context
    )




# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logout successful")
#     return redirect("userauths/signout.html")

def logout_view(request):
    logout(request)

    messages.success(request, "Logout successful")

    return render(request, "userauths/signin.html")
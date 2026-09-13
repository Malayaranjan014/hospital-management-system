from django.shortcuts import render

from doctor import models as doctor_models
from base import models as base_models
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)
    # featch all the notifications 
    notifications = doctor_models.Notification.objects.filter(doctor=doctor)

    context = {
        "appointments": appointments,
        "notifications": notifications,
    }

    return render(request, "doctor/dashboard.html", context)



# @login_required
# def appointments(request):
#     doctor = doctor_models.Doctor.objects.get(user=request.user)
#     appointments = base_models.Appointment.objects.filter(doctor=doctor)

#     context = {
#         "appointments": appointments,
#     }

#     return render(request, "doctor/appointments.html", context)
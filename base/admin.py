from django.contrib import admin
from base import models
# Register your models here.
from import_export.admin import ImportExportModelAdmin


#we can  add and edit medical records directly inside an appointment page.
class AppointmentInline(admin.TabularInline):
    model = models.Appointment
    extra = 1

class MedicalRecordInline(admin.TabularInline):
    model = models.MedicalRecord
    extra = 1

class LabTestInline(admin.TabularInline):
    model = models.LabTest
    extra = 1

class PrescriptionInline(admin.TabularInline):
    model = models.Prescription
    extra = 1

class BillingInline(admin.TabularInline):
    model = models.Billing
    extra = 1


# customize the service in admin pages 
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ['name', 'cost']
    search_fields = ['name', 'description']
    filter_horizontal = ['available_doctors']



        # its control the appointment admin page  
        #   Patient | Doctor | Appointment Date | Status  .its dipsly like this 
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'status']
    search_fields = ['patient__username', 'doctor__user__username']
    inlines = [MedicalRecordInline, LabTestInline, PrescriptionInline, BillingInline]


    # controls how the  columns appear for medical record 

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'diagnosis']

class LabTestAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'test_name']

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'medications']

# class BillingAdmin(admin.ModelAdmin):
#     list_display = ['patient','service_name', 'total', 'status', 'date']


class BillingAdmin(admin.ModelAdmin):

    list_display = [
        'billing_id',
        'patient',
        'service_name',
        'doctor_name',
        'sub_total',
        'tax',
        'total',
        'status',
        'date',
    ]

    search_fields = [
        'billing_id',
        'patient__full_name',
        'appointment__service__name',
        'appointment__doctor__full_name',
    ]

    list_filter = [
        'status',
        'date',
    ]

    ordering = ['-date']

    def service_name(self, obj):

        if obj.appointment and obj.appointment.service:
            return obj.appointment.service.name

        return "N/A"

    service_name.short_description = "Service"

    def doctor_name(self, obj):

        if obj.appointment and obj.appointment.doctor:
            return obj.appointment.doctor.full_name

        return "N/A"

    doctor_name.short_description = "Doctor"





# register the model 
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.MedicalRecord, MedicalRecordAdmin)
admin.site.register(models.LabTest, LabTestAdmin)
admin.site.register(models.Prescription, PrescriptionAdmin)
admin.site.register(models.Billing, BillingAdmin)


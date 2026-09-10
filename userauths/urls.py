
from django.urls import path
from userauths import views 


app_name="userauths"
urlpatterns = [
    path("signup/",views.register_view,name="signup"),    #signup page
    path("signin/",views.login_view,name="signin"),    #signin page
    path("signout/",views.logout_view,name="signout"),    #signout page
]
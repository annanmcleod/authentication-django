from django.urls import path
from . import views


urlpatterns = [
    path("log_in/", views.log_in, name="log_in"),
    path("log_out/", views.log_out, name="log_out"),
    path("sign_up/", views.signup, name="sign_up"),
    path("", views.home, name="home"),
    path("create/", views.createProfile, name="createProfile"),
    path("update/", views.updateProfile, name="updateProfile"),
    path("delete/", views.deleteProfile, name="deleteProfile"),
]

# path("log-in/", log_in, name="log-in"),
# path("log-out/", log_out, name="log-out"),
# path("signup/", sign up, name="signup"),

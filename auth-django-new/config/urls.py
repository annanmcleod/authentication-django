from account import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sign_up/", views.signup, name="sign_up"),
    path("home/", views.home, name="home"),
    path("", views.log_in, name="log_in"),
    path("log_out/", views.log_out, name="log_out"),
    path("create/", views.createProfile, name="createProfile"),
    path("update/<str:pk>/", views.updateProfile, name="updateProfile"),
    path("delete/<str:pk>/", views.deleteProfile, name="deleteProfile"),
]

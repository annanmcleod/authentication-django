from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only

# from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .forms import *
from .models import Profile


def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"{user} has created an account.")
            # group = Group.objects.get(name="profiler")
            # user.groups.add(group)
            return redirect("log_in")

    context = {"form": form}
    return render(request, "signup.html", context)


def log_in(request):
    # form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(
                request, "Username OR Password is incorrect. Please try again."
            )

    context = {}
    return render(request, "login.html", context)


def log_out(request):
    logout(request)
    return redirect("log_in")


@login_required(login_url="log_in")
# @admin_only
# @allowed_users(allowed_roles=["admin"])
def home(request):

    profiles = Profile.objects.all()

    context = {
        "profiles": profiles,
    }

    return render(request, "homepage.html", context)


@login_required(login_url="log_in")
def createProfile(request):
    form = CreateProfileForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            prof = form.save()
            prof.creator = request.user
            prof.save()
            return redirect("home")

    return render(request, "create.html", context)


@login_required(login_url="log_in")
# @admin_only
def updateProfile(request, pk):
    profiles = Profile.objects.get(id=pk)
    form = CreateProfileForm(instance=profiles)

    if request.method == "POST":
        form = CreateProfileForm(request.POST, instance=profiles)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "update.html", context)


@login_required(login_url="log_in")
# @admin_only
def deleteProfile(request, pk):
    profiles = Profile.objects.get(id=pk)

    if request.method == "POST":
        profiles.delete()
        return redirect("home")

    context = {"item": profiles}
    return render(request, "delete.html", context)

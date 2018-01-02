from django.shortcuts import render, redirect, HttpResponse
from .models import *


# Create your views here.
def index(request):
    if request.method == "GET":
        context = {
            "users":  User.objects.all()
        }

        return render(request, "users/index.html", context)


def show(request, user_id):
    # print "Show View Method"
    # print request.method
    if request.method == "GET":
        context = {
            "user": User.objects.get(id=user_id)
        }

        return render(request, "users/show.html", context)

def edit(request, user_id):
    # print "Edit View Method"
    # print request.method
    if request.method == "GET":
        context = {
            "user": User.objects.get(id=user_id),
            "edit": True
        }

        return render(request, "users/show.html", context)
    else:
        user = User.objects.get(id=user_id)
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        return redirect("/users/")

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/users/")


def new(request):
    return render(request, "users/new.html")

def create(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    User.objects.create(username=username, first_name=first_name, last_name=last_name)

    return redirect("/users/")

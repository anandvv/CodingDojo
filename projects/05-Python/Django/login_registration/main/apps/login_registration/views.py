from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    if not request.session['userid'] or 'userid' in request.session:
        request.session['userid'] = -1

    context = {
        'userid': request.session['userid']
    }
    return render(request, "login_registration/index.html", context)


def register(request):
    print "Register View"
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return render(request, "login_registration/index.html")

    #if all the registration fields are good, register, auto login, and show success page
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.filter(email=email).first()
        if not user:
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hash1)
            request.session['userid'] = user.id
            return redirect("/login/success")
        else:
            messages.error(request, "User already exists")
            return render(request, "login_registration/index.html")


def login(request):
    print "Login View"
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        if len(username) > 0:
            user = User.objects.filter(email=username).first()

            if user:
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    request.session['userid'] = user.id
                    request.session['username'] = user.email
                    messages.success(request, "Successful Login!")
                    return redirect("/login/success")
                else:
                    messages.error(request, "Incorrect Password!")
                    return render(request, "login_registration/index.html")
            else:
                messages.error(request, "Incorrect Email!")
                return render(request, "login_registration/index.html")
        else:
            messages.error(request, "Please enter email address")
            return render(request, "login_registration/index.html")


def success(request):
    context = {
        'userid': request.session['userid']
    }
    return render(request, "login_registration/success.html", context)


def logout(request):
    request.session['userid'] = -1
    return redirect("/login/")
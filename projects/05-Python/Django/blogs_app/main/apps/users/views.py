from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Place to display all the users')

def new(request):
    return redirect('/register')

def register(request):
    response = "Placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "Placeholder for users to login"
    return HttpResponse(response)
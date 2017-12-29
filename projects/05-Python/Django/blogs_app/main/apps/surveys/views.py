from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Surveys Index File')

def new(request):
    return HttpResponse('Placeholder for users to add a new survey!')
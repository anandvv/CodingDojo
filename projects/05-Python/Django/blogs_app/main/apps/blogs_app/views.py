from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def display(request):
    response = "Placeholder to display all blogs!"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to create a new blog entry!"
    return HttpResponse(response)

def create(request):
    return redirect("/blogs_app/")

def show(request, blog_id):
    response = "Placeholder to show blog entry " + blog_id
    return HttpResponse(response)

def edit(request, blog_id):
    response = "Placeholder to edit blog entry " + blog_id
    return HttpResponse(response)

def delete(request, blog_id):
    response = "Placeholder to delete blog entry " + blog_id
    return HttpResponse(response)

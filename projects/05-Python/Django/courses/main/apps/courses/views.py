from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse('index')
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses/index.html", context)


def new(request):
    courseErrors = Course.objects.basic_validator(request.POST)
    if len(courseErrors):
        for tag, error in courseErrors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses/')

    descriptionErrors = Description.objects.basic_validator(request.POST)
    if len(descriptionErrors):
        for tag, error in descriptionErrors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses/')

    if request.method == "POST":
        course_name = request.POST['name']
        description = request.POST['description']

        course = Course.objects.create(course_name=course_name)
        Description.objects.create(description=description, course=course)

        return redirect("index")


def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect("/courses/")
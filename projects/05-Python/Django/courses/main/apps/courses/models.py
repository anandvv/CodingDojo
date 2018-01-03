from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        return errors


class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['description']) < 10:
            errors["description"] = "Description should be more than 10 characters"
        return errors


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = CourseManager()
    # *************************


class Description(models.Model):
    description = models.CharField(max_length=1000)
    course = models.OneToOneField(Course, related_name="description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = DescriptionManager()
    # *************************




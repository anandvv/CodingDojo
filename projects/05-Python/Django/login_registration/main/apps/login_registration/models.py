from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters"
        if not postData['password'] == postData['password_again']:
            errors["password"] = "passwords do not match"

        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



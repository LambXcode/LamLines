from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.account_type})"

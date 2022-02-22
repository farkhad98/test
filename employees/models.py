from django.db import models
from django.db.models.base import Model
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class EmployeeGroup(models.Model):
    name = models.CharField(max_length=255)
    system_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

# As a profile
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(EmployeeGroup, related_name='employees')
    phone = models.CharField(max_length=255)
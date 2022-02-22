from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from crm_project.employees.models import Employee
from crm_project.customers.models import Customer

class Subject(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    system_name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

class Group(models.Model):
    teacher = models.ForeignKey(Employee, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    archived = models.BooleanField(default=False)

class Student(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    archived = models.BooleanField(default=False)

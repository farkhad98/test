from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from crm_project.models.academy import Student
from crm_project.models.employees import Employee
from django.contrib.auth.models import User

class TransactionCategory(models.Model):
    name = models.CharField(max_length=255)
    system_name = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255) #withdraval or income, or inside operations

class PaymentType(models.Model):
    name = models.CharField(max_length=255)
    system_name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

# As a profile
class Transaction(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
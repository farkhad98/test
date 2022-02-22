from datetime import date
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Kanban stage
class Stage(models.Model):
    name = models.CharField(max_length=255)
    system_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    sort = models.IntegerField(default=0)

class Customer(models.Model):
    manager = models.ForeignKey(User, on_delete=models.PROTECT)
    stage = models.ForeignKey(Stage, on_delete=models.PROTECT)
    archived = models.BooleanField(default=False)
    customer = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=13)
    passport_no = models.CharField(max_length=9)
    

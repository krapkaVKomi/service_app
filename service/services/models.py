from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )
    
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])


class Subscripthion(models.Model):
    client = models.ForeignKey(Client, related_name='subscripthion', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscripthion', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscripthion', on_delete=models.PROTECT)
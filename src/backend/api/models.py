# backend/models.py

from django.db import models


class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    stock_status = models.CharField(max_length=50)
    available_stock = models.IntegerField()


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    merchant = models.CharField(max_length=255)
    date = models.DateField()
    approved = models.BooleanField()


class Employee(models.Model):
    id = models.UUIDField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    extras = models.IntegerField()

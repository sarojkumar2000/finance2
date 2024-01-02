# models.py
from django.db import models

class admin(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=25)
    phone = models.CharField(max_length=10, default='N/A')

    class Meta:
        db_table = "Admin"



class Users(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=5, decimal_places=2)
    proof = models.CharField(max_length=255)
    address = models.TextField()
    loan_type = models.CharField(max_length=10, choices=[('monthly', 'Monthly'), ('daily', 'Daily')])
    applied_date = models.DateField(null=True)
    next_due = models.IntegerField(default=0)
    next_due_date = models.DateField()
    tenure = models.IntegerField(default=0)
    lastpaid=models.DateField(null=True)
    interest_amount=models.IntegerField(default=0)

    class Meta:
        db_table = "Users"

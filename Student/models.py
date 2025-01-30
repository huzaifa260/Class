from django.db import models


# Create your models here.

class Student(models.Model):
    sr = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    std = models.CharField(max_length=200, blank=True, null=True)
    admission_date = models.CharField(max_length=200, blank=True, null=True)
    total_fees = models.IntegerField(blank=True, null=True)
    paid_fees = models.IntegerField(blank=True, null=True)
    outstanding_fees = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.std}"


class user(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"


class Receipt(models.Model):
    sr = models.IntegerField(blank=True, null=True)
    receipt_date = models.CharField(max_length=50, blank=True, null=True)
    stud_name = models.CharField(max_length=100, blank=True, null=True)
    rs = models.CharField(max_length=100, blank=True, null=True)
    std = models.CharField(max_length=30, blank=True, null=True)
    tot_amount_due = models.CharField(max_length=30, blank=True, null=True)
    amount_recived = models.CharField(max_length=30, blank=True, null=True)
    balance_due = models.CharField(max_length=30, blank=True, null=True)
    payment_received_in = models.CharField(max_length=150, blank=True, null=True)
    received_by = models.CharField(max_length=100, blank=True, null=True)

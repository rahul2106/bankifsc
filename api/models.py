# bankdetails/models.py
from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=11, unique=True)
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city1 = models.CharField(max_length=50)
    city2 = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    std_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.ifsc

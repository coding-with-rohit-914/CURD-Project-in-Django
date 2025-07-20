from django.db import models

class StudentData(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cource = models.CharField(max_length=30)
    fee = models.IntegerField()
    iname = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    a4 = models.IntegerField()
    loc = models.CharField(max_length=30)

from django.db import models

class Student_register(models.Model):
    regno  = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=50)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50,unique=True)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

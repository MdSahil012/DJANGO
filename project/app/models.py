from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    contact=models.IntegerField()
    City=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)
    CPassword=models.CharField(max_length=20,null=True)
    Photo=models.ImageField(upload_to='image')
    Audio=models.FileField(upload_to='audio')
    Video=models.FileField(upload_to='video')
    Resume=models.FileField(upload_to='document')
    Qualification=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    
class Department(models.Model):
    dep_name=models.CharField(max_length=40)
    dep_desc=models.CharField(max_length=40)
    dep_head=models.CharField(max_length=40)

class Add_Employee(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField()
    Contact=models.BigIntegerField()
    Image=models.ImageField(upload_to='image')
    Code=models.CharField(max_length=20)
    Dept=models.CharField(max_length=20)

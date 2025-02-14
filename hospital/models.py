
# # Create your models here.
# from django.db import models
# import uuid

# class Patient(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     contact_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.TextField()
#     problem = models.CharField(max_length=255)

# class Doctor(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     contact_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.TextField()
#     specialization = models.CharField(max_length=100)
#     experience = models.IntegerField()

# class Report(models.Model):
#     id = models.AutoField(primary_key=True)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     report_file = models.FileField(upload_to='reports/')

# class APIKey(models.Model):
#     id = models.AutoField(primary_key=True)
#     key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
import uuid

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    problem = models.CharField(max_length=255)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='reports/')

from django.db import models
import uuid

class APIKey(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=40, default="xxxxx")

    def __str__(self):
        return f"{self.user} - {self.key}"


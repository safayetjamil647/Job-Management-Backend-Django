from django.db import models
from django.db.models.deletion import CASCADE
from rest_framework import serializers
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default='',null=False,unique=True)
    company_name = models.CharField(max_length=50, blank=False, default='')
    company_email= models.EmailField(max_length=50,blank=False)
    linkedin_url = models.URLField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name
        
class Category(models.Model):
    name=models.CharField(max_length=20,blank=False, default='')
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=20,blank=False, default='')
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Tech(models.Model):
    name=models.CharField(max_length=20,blank=False, default='')
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='',null=False)
    job_title = models.CharField(max_length=50,blank=False, default='')
    job_location=models.CharField(max_length=20,blank=False)
    job_description=models.TextField(max_length=400,blank=False)
    created_at = models.DateTimeField(auto_now=True)
    posted_at = models.DateField(auto_now=True)
    deadline_at = models.DateField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE,primary_key=True,null=False,default='',unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default='',null=False)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,default='',null=False)
    tech=models.ForeignKey(Tech,on_delete=models.CASCADE,default='',null=False)
    def __str__(self):
        return self.job_title



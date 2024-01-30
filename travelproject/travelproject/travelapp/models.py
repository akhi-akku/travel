from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

def __str__(self):
        return self.name
class People(models.Model):
    pname=models.CharField(max_length=250)
    pimg=models.ImageField(upload_to='pics')
    relation=models.CharField(max_length=250)
    pdesc=models.TextField()

def __str__(self):
        return self.pname


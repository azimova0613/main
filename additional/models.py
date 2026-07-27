from django.db import models

# Create your models here.

class dacha(models.Model):
    image=models.ImageField(upload_to='images/')
    nomi=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    soni=models.IntegerField()
    narx=models.IntegerField()
    date=models.DateField()
    date2=models.DateTimeField(auto_now_add=True)

class uzum_market(models.Model):
    image=models.ImageField(upload_to='images/')
    nomi=models.CharField(max_length=30)
    narx=models.IntegerField()
    soni=models.IntegerField()
    chegirma=models.IntegerField()
    title=models.CharField(max_length=100)

class kompyuter(models.Model):
    image=models.ImageField(upload_to='images/')
    brend=models.CharField(max_length=50)
    modeli=models.CharField(max_length=30)
    prosessor=models.CharField(max_length=10)
from django.db import models

# Create your models here.

class TourGuide(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self):
        return self.name + ' ' + self.surname

class Travel(models.Model):
    destination = models.CharField(max_length=64,unique=True)
    price = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    tourGuide = models.ForeignKey(to=TourGuide,on_delete=models.CASCADE,related_name='destinations')

    def __str__(self):
        return self.destination

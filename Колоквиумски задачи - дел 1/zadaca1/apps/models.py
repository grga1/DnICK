from django.db import models

# Create your models here.
class Baker(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self):
        return self.name+' '+self.surname


class Cake(models.Model):
    name = models.CharField(max_length=64,unique=True)
    price = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    baker = models.ForeignKey(to=Baker,on_delete=models.CASCADE,related_name='cakes')

    def __str__(self):
        return self.name


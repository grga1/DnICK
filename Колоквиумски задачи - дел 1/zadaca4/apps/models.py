from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.CharField(max_length=30)
    linkedIn = models.URLField()
    sales = models.PositiveIntegerField(default=0)
    email = models.EmailField()

    def __str__(self):
        return self.name + ' ' + self.surname


class Characteristic(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Estate(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)
    area = models.DecimalField(max_digits=6, decimal_places=2)
    saleDate = models.DateField()
    image = models.ImageField(upload_to='images/')
    reserved = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)

    agents = models.ManyToManyField(Agent, related_name='estates')
    characteristics = models.ManyToManyField(Characteristic, related_name='estates', blank=True)


    def price(self):
        return sum(c.price for c in self.characteristics.all())

    def __str__(self):
        return   self.name+' '+f"{self.area}m2 - {self.description}"
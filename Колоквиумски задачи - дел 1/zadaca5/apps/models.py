from django.db import models

# Create your models here.

class Avtor(models.Model):
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)
    email = models.EmailField()
    def __str__(self):
        return self.ime+' '+self.prezime

class Kupuvac(models.Model):
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)
    email = models.EmailField()
    def __str__(self):
        return self.ime+' '+self.prezime

class Kniga(models.Model):
    naslov = models.CharField(max_length=64)
    opis = models.TextField()
    cena = models.DecimalField(decimal_places=2,max_digits=6)
    slika = models.ImageField(upload_to='images/')
    avtori= models.ManyToManyField(to=Avtor,related_name="knigi")
    def __str__(self):
        return self.naslov

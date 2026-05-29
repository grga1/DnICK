
from django.db import models
# Create your models here.

class Umetnik(models.Model):
    stil = [
        ('impressionism', 'IMPRESSIONISM'),
        ('pop art', 'POP ART'),
        ('graffiti', 'GRAFFITI'),
    ]
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)
    umetnickiStil = models.CharField(max_length=20, choices=stil)
    email = models.EmailField()
    def __str__(self):
        return self.ime + ' ' + self.prezime

class Izlozba(models.Model):
    naslov = models.CharField(max_length=64)
    datumNaPocetok = models.DateField()
    datumNaZavrsuvanje = models.DateField()
    opis = models.TextField()
    lokacija = models.CharField(max_length=20)

    def __str__(self):
        return self.naslov


class UmetnickoDelo(models.Model):
    naslov = models.CharField(max_length=64)
    datumNaSozdavanje = models.DateField()
    slika = models.ImageField(upload_to='images/')
    izlozba = models.ForeignKey(to=Izlozba,on_delete=models.CASCADE, related_name="umetnickodelo")
    umetnik = models.ForeignKey(to=Umetnik,on_delete=models.CASCADE)

    def __str__(self):
        return self.naslov

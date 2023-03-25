from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    foto = models.ImageField(default='generic_profile_pic.png')

class Student(User):
    
    COUNTRY_CHOICES = [
        ('United States', 'United States'),
        ('England', 'England'),
        ('Australia', 'Australia')
    ]

    country = models.CharField(max_length=13, choices=COUNTRY_CHOICES, default='Student')

class Teacher(User):
    age = models.IntegerField()

class Clase(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clases_a_ensenar')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clases_a_aprender')

class Disponible(models.Model):

    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    dia = models.CharField(max_length=9, choices=DAYS_CHOICES)
    hora = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class Payment(models.Model):
    fecha = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    creditos = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
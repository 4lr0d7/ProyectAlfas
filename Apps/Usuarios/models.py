from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    PAISES =[
        ('MX' , 'Mexico'),
        ('EU' , 'Estados Unidos')
    ]

    is_premium = models.BooleanField(default=False, null=False, blank=False)
    fechaNacimiento = models.DateField(auto_now_add=False, null=True, blank = True)
    pais = models.CharField(max_length=10, choices = PAISES, default = 'Mexico', null=True, blank=False)
    foto = models.ImageField(upload_to = 'uploads/', blank=True, null=True)
    is_artist = models.BooleanField(default=False, null=False, blank=True)
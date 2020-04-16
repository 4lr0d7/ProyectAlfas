import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
def images_path():
    return os.path.join(settings.STATICFILES_DIRS, 'img/disc_photos1')

# Create your models here.
class Cancion (models.Model):
    nombre = models.CharField(max_length = 50)
    duracion = models.DecimalField(max_digits = 4, decimal_places = 2)
    autor = models.CharField(max_length = 100)
    calificacion = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)
    album = models.ForeignKey('Album', on_delete =models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.album)

    class Meta:
        verbose_name = "Cancion"
        verbose_name_plural = "Canciones"

class Album (models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    duracion = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)
    fecha = models.DateField(auto_now = False, auto_now_add = False)
    foto = models.ImageField(upload_to = images_path, max_length = 100, null = True, blank = True)
    generos = models.ForeignKey('Generos', on_delete = models.CASCADE)
    disquera = models.ForeignKey('Disquera', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albumes"

class Disquera (models.Model):
    nombre = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Disquera"
        verbose_name_plural = "Disqueras"



class Playlist(models.Model):
     nombre = models.CharField(max_length = 250)
     is_public = models.BooleanField()
     usuario = models.ForeignKey(User, on_delete = models.CASCADE)

    #def __str__(self):
    #    return self.nombre

     class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"


class PlaylistCanciones(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete = models.CASCADE)
    Cancion = models.ForeignKey('Cancion', on_delete = models.CASCADE)
    class Meta:
        verbose_name = "PlaylistCancion"
        verbose_name_plural = "PlaylistCanciones"

class UsuarioCanciones(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    Cancion = models.ForeignKey('Cancion', on_delete = models.CASCADE)
    class Meta:
        verbose_name = "UsuarioCancion"
        verbose_name_plural = "UsuarioCanciones"


class Generos(models.Model):
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

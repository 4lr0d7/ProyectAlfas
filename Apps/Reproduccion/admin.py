from django.contrib import admin
from .models import Cancion, Album, Disquera, Playlist, PlaylistCanciones, UsuarioCanciones, Generos

# Register your models here.
admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Disquera)
admin.site.register(Playlist)
admin.site.register(PlaylistCanciones)
admin.site.register(UsuarioCanciones)
admin.site.register(Generos)
from django.shortcuts import render

def home (request):
    return render(request, 'home_artista.html')
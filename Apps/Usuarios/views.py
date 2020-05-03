from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from Apps.Reproduccion import views as views_reproduccion
#from django.contrib.auth.models import User 
from Apps.Usuarios.models import User
#HTTPRESPONSE - JSONRESPONSE - RENDER

# Create your views here.

def Loginn(request):
     if request.method == "POST":

          form = LoginForm(request.POST)
          if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user = authenticate(request, username=username, password=password)
               print(user)
               if user is not None:
                    login(request, user)
                    return redirect (views_reproduccion.home)
               else:
                    form.add_error(None, 'Revisa tus datos')
                    return render(request, 'login.html', {'form':form})

          else:
               return HttpResponse('Datos invalidos en tu formulario')

     else:
          form = LoginForm()
          return render(request, 'login.html', {'form':form})


def register(request):
     if request.method == 'POST':
          form = RegisterForm(request.POST)

          if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               email = form.cleaned_data['email']
               nombre = form.cleaned_data['first_name']
               apellido = form.cleaned_data['last_name']
               fechaNacimiento = form.cleaned_data['fechaNacimiento']
               pais = form.cleaned_data['pais']
               foto = form.cleaned_data['foto']
               is_artist = form.cleaned_data['is_artist']

               user,created = User.objects.get_or_create(
                    username = username,
                    email = email
               )

               if created:
                    user.first_name = nombre
                    user.last_name = apellido
                    user.fechaNacimiento = fechaNacimiento
                    user.pais = pais
                    user.foto = foto
                    user.is_artist = is_artist
                    user.set_password(password)
                    user.save()
                    form.add_error(None, "Usuario creado exitosamente")
                    return render(request, 'register.html', {'form':form})
               else:
                    return render(request, 'register.html', {'form':form})

          else: 
               return render(request, 'register.html', {'form':form})
          
     else:
          form = RegisterForm()
          return render(request, 'register.html',{'form':form})

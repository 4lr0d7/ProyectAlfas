from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from Apps.Reproduccion import views as views_reproduccion
from django.contrib.auth.models import User 
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
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']

                user, created = User.objects.get_or_create(
                     username = username,
                     email = email
                )
                     
                if created:
                     form.add_error(None, '¡Usuario creado exitosamente!')
                else:
                     form.add_error(None, '¡Ya existe un Usuario con el mismo nombre o el mismo correo!')
                     return render (request, 'register.html', {'form':form})


          else:
               return render (request, 'register.html', {'form':form})

     else:
          form = RegisterForm()
          return render (request, 'register.html', {'form':form})
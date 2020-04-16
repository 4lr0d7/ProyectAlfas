from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100, label = 'Ingresa tu usuario' , min_length = 5, required = True, widget = forms.TextInput(attrs={'placeholder':'Ingrese su usuario', 'class':'form-control'}))
    password = forms.CharField(max_length = 100, label = 'Ingresa tu contraseña' ,min_length = 5, required = True, widget = forms.PasswordInput(attrs={'placeholder':'Ingrese su contraseña', 'class':'form-control'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','username', 'password', 'email']
        labels = {
            'first_name' : "Nombres",
            'last_name' : 'Apellidos',
            'username' : 'Nombre de Usuario',
            'password' : 'Contraseña',
            'email' : 'Correo Electrónico'
        }
        widgets = {
            'first_name' :forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Inserte sus nombres'}),
            'last_name' : forms.TextInput(attrs ={'class' : 'form-control', 'placeholder' : 'Inserte sus apellidos'}),
            'username' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Inserte un nombre de Usuario'}),
            'password' : forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Inserte una contraseña'}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder' : 'Inserte su correo electrónico'})
        }
        help_texts={
            'username' : 'Máximo 150 carácteres (NOTA: Sólo insertar letras y números)',
            'password' : 'Por su seguridad: use al menos una letra en mayúscula, algún signo y números',
            'email' : 'ejemplo@ejemplo.com',
        }
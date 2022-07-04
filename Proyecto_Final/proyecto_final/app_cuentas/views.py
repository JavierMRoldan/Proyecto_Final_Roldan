from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from app_cuentas.models import Avatar
from django.contrib.auth.models import User

# Create your views here.
def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request, user)
                return render(request , "inicio.html" , {"mensaje":f"Bienvenido {usuario}"})
                #avatares = Avatar.objects.filter(user=request.user.id)
                #return render(request, "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse("Usuario")


    form = AuthenticationForm()

    return render (request , "login.html", {"form":form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect(to='login')

    else:
        form = UserRegisterForm()
    return render( request , "registro.html", {"form":form})



@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")

    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request , "editar_perfil.html", {"mi_formulario":mi_formulario , "usuario":usuario})

@login_required
def inicio(request):
    
    return render(request, "inicio.html")
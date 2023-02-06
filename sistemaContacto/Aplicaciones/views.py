from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def elements(request):
    return render(request, 'dashboard/elements.html')


def Inscripciones(request):
    return render(request, 'dashboard/form_basic.html')


def crear_evento(request):
    return render(request, "dashboard/crear-event.html")


def autent_qr(request):
    return render(request, "dashboard/autent_qr.html")


def event_creado(request):
    return render(request, "dashboard/event_creado.html")

def charts(request):
    return render(request, "dashboard/charts.html")
# REGISTRO
def signup(request):
    if request.method == 'GET':
        return render(request, 'dashboard/authentication-register.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('lognin')
            except IntegrityError:
                return render(request, 'dashboard/authentication-register.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'dashboard/authentication-register.html', {"form": UserCreationForm, "error": "Passwords did not match."})


# cerrrar sesion

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

# login


def signin(request):
    if request.method == 'GET':
        return render(request, 'dashboard/authentication-login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dashboard/authentication-login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('dashboard/index.html')

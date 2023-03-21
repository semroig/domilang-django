from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import User


def index(request):
    return render(request, "mvp/index.html")

def arrange(request):
    all_users = User.objects.filter(type='Teacher')
    return render(request, "mvp/arrange.html", {
        "usuarios": all_users
    })

def home(request):
    return render(request, "mvp/home.html")

def packs(request):
    return render(request, "mvp/packs.html")

def payments(request):
    return render(request, "mvp/payments.html")

def profile(request):
    return render(request, "mvp/profile.html")

def teacher(request, teacher_id):
    reg = User.objects.get(id=teacher_id)
    return render(request, "mvp/teacher.html", {
        "registro": reg
    })

@api_view(['POST'])
def login_view(request):

    # Attempt to sign user in
    body = request.data
    username = body["username"]
    password = body["password"]
    user = authenticate(request, username=username, password=password)

    # Check if authentication successful
    if user is not None:
        login(request, user)
        return Response(status=status.HTTP_200_OK, data={"message": "successful login"})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message": "invalid credentials"})

@api_view(['POST'])
def register(request):

    # Parseo data
    body = request.data
    username = body["username"]
    email = body["email"]

    # Ensure password matches confirmation
    password = body["password"]
    confirmation = body["confirmation"]
    if password != confirmation:
        # La contraseña y la confirmación no son iguales
        data={"message": "password and confirmation must match"}
        return Response(status=status.HTTP_412_PRECONDITION_FAILED, data=data)

    # Attempt to create new user
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except IntegrityError:
        # El username ya existe
        data={"message": "Username already taken."}
        return Response(status=status.HTTP_409_CONFLICT, data=data)

    # Además de registrarlo, ya se logea
    login(request, user)
    data={"message": "successful sign up"}
    return Response(status=status.HTTP_200_OK, data=data)

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
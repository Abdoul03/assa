from django.shortcuts import render

# Create your views here.

def sign_in(request):
    return render(request,'connection/sign_in.html')


def sign_up(request):
    return render(request,'connection/sign_up.html')


def medecin(request):
    return render(request,'connection/medecin.html')


def patients(request):
    return render(request,'connection/patient.html')
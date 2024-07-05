from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
#inscription_medecin
#from .forms import medecin_form
from connection.models import Medecin

# Create your views here.

def sign_in(request):
    return render(request,'connection/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        #form = medecin_form(request.POST)
        if Medecin:
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            adresse = request.POST['adresse']
            email = request.POST['email']
            #specialite = request.POST['specialite']
            telephone = request.POST['telephone']
            mot_de_passe = request.POST['mot_de_passe']
            
            # Save to Database? 
            medecin = Medecin(nom=nom, prenom=prenom, adresse=adresse, email=email, telephone=telephone, mot_de_passe=mot_de_passe)
            medecin.save()
    return render(request,'connection/sign_up.html')



def medecin(request):
    return render(request,'connection/medecin.html')


def patients(request):
    return render(request,'connection/patient.html')

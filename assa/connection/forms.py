from django import forms

from connection.models import Medecin


class medecin_form(forms.Form):
    # some widget stuff here
    class Meta:
        model = Medecin
        fields = ('nom', 'prenom', 'email', 'adresse', 'telephone', 'mot_de_passse')
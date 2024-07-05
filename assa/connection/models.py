from django.db import models

# Create your models here.
class Medecin(models.Model):
  prenom = models.CharField(max_length=255)
  nom = models.CharField(max_length=255)
  adresse = models.CharField(max_length=255)
  email = models.EmailField()
  specialite = models.CharField(max_length=255)
  telephone = models.IntegerField()
  mot_de_passe = models.CharField(max_length=255)

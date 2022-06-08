from django.db import models

# Create your models here.
class cliente (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def str (self):
        return self.nome
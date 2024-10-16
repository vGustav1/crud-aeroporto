from django.db import models

class Airplane(models.Model):
  matricula = models.CharField(max_length=5)
  numero_Voo = models.CharField(max_length=4)
  modelo = models.CharField(max_length=4)
  procedencia = models.CharField(max_length=3)
  destino = models.CharField(max_length=3)
  numero_passageiros = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.modelo} {self.matricula} {self.procedencia} {self.destino}"
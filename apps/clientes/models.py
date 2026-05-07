from django.db import models

#create your models here

class Cliente(models.Model):
    nome = models.CharField(verbose_name="nome completo", max_length=100)
    cpf = models.CharField(verbose_name="CPF", max_length=14)
    telefone = models.CharField(verbose_name="telefone",max_length=14)
    nascimento = models.DateField(verbose_name="data de nascimento")

    def __str__(self):
        return self.nome
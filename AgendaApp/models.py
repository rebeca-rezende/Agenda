from django.db import models

# Create your models here.
class Agenda(models.Model):

    ESTADOS_CIVIS = [
        ('S', 'Solteiro'),
        ('C','Casado'),
        ('D','Divorciado'),
        ('V','Viúvo')
        ]

    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    DataNascimento = models.DateField(verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=1, choices=ESTADOS_CIVIS, null=True)



    def __str__ (self):
        return self.nome
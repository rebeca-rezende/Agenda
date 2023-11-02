from django.db import models

# Create your models here.
UFS = [
        ('SP', 'São Paulo'),
        ('MG', 'Minas Gerais'),
        ('RJ', 'Rio de Janeiro'),
        ('Es', 'Espírito Santo')
    ]

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UFS)

    def __str__ (self):
        return self.nome
    
class Agenda(models.Model):

    ESTADOS_CIVIS = [
        ('S', 'Solteiro'),
        ('C','Casado'),
        ('D','Divorciado'),
        ('V','Viúvo')
    ]

 
    

    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    DataNascimento = models.DateField(verbose_name="Data de Nascença")
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=UFS)
    estado_civil = models.CharField(max_length=1, choices=ESTADOS_CIVIS, null=True)



    def __str__ (self):
        return self.nome

class Telefone(models.Model):

    TIPOS_TELEFONE = [
        ('RES', 'Residencial'),
        ('COM', 'Comercial'),
        ('REC', 'Recado'),
        ('CEL', 'Celular')
    ]

    contato = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    numero = models.CharField(max_length=10) 
    tipo = models.CharField(max_length=3, choices=TIPOS_TELEFONE)
    IsWhatsapp = models.BooleanField(verbose_name="Tem Whatsapp? ")
    
    
    def __str__ (self):
        return f'({self.ddd}) {self.numero}'
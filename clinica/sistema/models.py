from django.db import models
# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

class Paciente (models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=60)
    cpf = models.CharField(unique=True, max_length=14)
    telefone = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

class Medico (models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=60)
    cpf = models.CharField(unique=True, max_length=14)
    telefone = models.CharField(max_length=15)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Consulta (models.Model):
    data = models.DateTimeField(unique=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.data)
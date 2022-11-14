from tkinter import CASCADE
from django.db import models

class Departamento(models.Model):
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

class Habilitacao(models.Model):
    validade = models.DateField()
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

class Municipio(models.Model):
    uf = models.CharField(unique=False, max_length=2)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Corretor(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    comissao = models.DecimalField(max_digits=10, decimal_places=2)
    gerente = models.ForeignKey("Corretor", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Telefone(models.Model):
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    numero = models.CharField(max_length=13)

class Regiao(models.Model):
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nome

class CorretorAtendeRegiao(models.Model):
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

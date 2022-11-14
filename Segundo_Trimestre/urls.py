"""Segundo_Trimestre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Segundo_Trimestre.views import paginas

from Segundo_Trimestre.views.Questao_1 import funcionario
from Segundo_Trimestre.views.Questao_1 import departamento

from Segundo_Trimestre.views.Questao_2 import pessoa
from Segundo_Trimestre.views.Questao_2 import habilitacao

from Segundo_Trimestre.views.Questao_3 import municipio, corretor, telefone, regiao, atende

urlpatterns = [
    # PÁGINA PRINCIPAL
    path('home', paginas.home, name='home'),

    # Questao 1

    path('funcionarios', funcionario.listar, name='funcionarios'),
    path('funcionarios/criar', funcionario.criar, name='funcionarios.criar'),
    path('funcionarios/editar/<id>', funcionario.editar, name='funcionarios.editar'),
    path('funcionarios/excluir/<id>', funcionario.excluir, name='funcionarios.excluir'),

    path('departamentos', departamento.listar, name='departamentos'),
    path('departamentos/criar', departamento.criar, name='departamentos.criar'),
    path('departamentos/editar/<id>', departamento.editar, name='departamentos.editar'),
    path('departamentos/excluir/<id>', departamento.excluir, name='departamentos.excluir'),

    # Questao 2

    path('pessoas', pessoa.listar, name='pessoas'),
    path('pessoas/criar', pessoa.criar, name='pessoas.criar'),
    path('pessoas/editar/<id>', pessoa.editar, name='pessoas.editar'),
    path('pessoas/excluir/<id>', pessoa.excluir, name='pessoas.excluir'),

    path('habilitacoes', habilitacao.listar, name='habilitacoes'),
    path('habilitacoes/criar', habilitacao.criar, name='habilitacoes.criar'),
    path('habilitacoes/editar/<id>', habilitacao.editar, name='habilitacoes.editar'),
    path('habilitacoes/excluir/<id>', habilitacao.excluir, name='habilitacoes.excluir'),

    # Questao 3

    path('corretora', paginas.homeCorretora, name='corretora'),

    path('municipios', municipio.listar, name='municipios'),
    path('municipios/criar', municipio.criar, name='municipios.criar'),
    path('municipios/editar/<id>', municipio.editar, name='municipios.editar'),
    path('municipios/excluir/<id>', municipio.excluir, name='municipios.excluir'),
    
    path('corretores', corretor.listar, name='corretores'),
    path('corretores/criar', corretor.criar, name='corretores.criar'),
    path('corretores/editar/<id>', corretor.editar, name='corretores.editar'),
    path('corretores/excluir<id>', corretor.excluir, name='corretores.excluir'),

    path('telefones', telefone.listar, name='telefones'),
    path('telefones/criar', telefone.criar, name='telefones.criar'),
    path('telefones/editar/<id>', telefone.editar, name='telefones.editar'),
    path('telefones/excluir<id>', telefone.excluir, name='telefones.excluir'),
    
    path('regioes', regiao.listar, name='regiaos'),
    path('regioes/criar', regiao.criar, name='regiaos.criar'),
    path('regioes/editar/<id>', regiao.editar, name='regiaos.editar'),
    path('regioes/excluir<id>', regiao.excluir, name='regiaos.excluir'),

    path('atendimentos', atende.listar, name='atendes'),
    path('atendimentos/criar', atende.criar, name='atendes.criar'),
    path('atendimentos/editar/<id>', atende.editar, name='atendes.editar'),
    path('atendimentos/excluir<id>', atende.excluir, name='atendes.excluir')

]
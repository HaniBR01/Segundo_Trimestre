from django.shortcuts import render


def home(request):
    '''
    Página inicial da aplicação
    '''
    return render(request, 'home.html', {})

def homeCorretora(request):
    ''' Questao 3'''
    return render(request, 'Questao-3/home.html',{
        "nome": "Gerenciamento de corretores"
    })
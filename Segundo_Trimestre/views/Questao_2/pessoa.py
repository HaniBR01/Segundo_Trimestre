from django.shortcuts import get_object_or_404, redirect, render
from Segundo_Trimestre.models import Pessoa
from django.forms import ModelForm

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

def listar(request):

    pessoas = Pessoa.objects.all()

    return render(request, 'Questao-2/Pessoa/listar.html',{
        'nome': 'Listar Pessoas',
        'pessoas': pessoas
    })

def criar(request):
    
    frm = PessoaForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('pessoas')

    return render(request, 'Questao-2/Pessoa/form.html',{
        'nome' : 'Cadastrar nova pessoa',
        'frm' : frm
    })

def editar(request, id):
    
    pessoa = get_object_or_404(Pessoa, pk=id)
    frm = PessoaForm(request.POST or None, instance=pessoa)

    if frm.is_valid():
        frm.save()
        return redirect('pessoas')

    return render(request, 'Questao-2/Pessoa/form.html',{
        'nome' : 'Editar uma pessoa',
        'frm' : frm
    })

def excluir(request, id):
    
    pessoa = get_object_or_404(Pessoa, pk=id)
    pessoa.delete()

    return redirect('pessoas')

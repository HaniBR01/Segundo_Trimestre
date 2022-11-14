from django.shortcuts import get_object_or_404, redirect, render
from Segundo_Trimestre.models import Funcionario
from django.forms import ModelForm

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

def listar(request):

    funcionarios =  Funcionario.objects.all()

    return render(request, 'Questao-1/Funcionarios/listar.html', {
        'nome': 'Listar Funcionarios',
        'funcionarios': funcionarios
    })


def criar(request):

    frm = FuncionarioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('funcionarios')

    return render(request, 'Questao-1/Funcionarios/form.html',{
        'nome' : 'Cadastrar funcionarios',
        'frm':frm
    })

def editar(request,id):
    '''
    Ação para editar uma categoria
    '''
    funcionario = get_object_or_404(Funcionario, pk=id)
    frm = FuncionarioForm(request.POST or None, instance=funcionario)

    if frm.is_valid():
        frm.save()
        return redirect('funcionarios')

    return render(request, 'Questao-1/Funcionarios/form.html',{
        'nome' : 'Editar funcionarios',
        'frm':frm
    })

def excluir(request,id):
    '''
    Exclui uma categoria do banco de dados
    '''
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()

    return redirect('funcionarios')
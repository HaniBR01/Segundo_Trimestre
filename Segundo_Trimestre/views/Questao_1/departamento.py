from django.shortcuts import get_object_or_404, redirect, render
from Segundo_Trimestre.models import Departamento
from django.forms import ModelForm

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

def listar(request):

    departamentos =  Departamento.objects.all()

    return render(request, 'Questao-1/Departamentos/listar.html', {
        'nome' : 'Listar Departamentos',
        'departamentos' : departamentos
    })

def criar(request):

    frm = DepartamentoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('departamentos')

    return render(request, 'Questao-1/Departamentos/form.html',{
        'nome' : 'Cadastrar Departamento',
        'frm':frm
    })

def editar(request,id):

    departamento = get_object_or_404(Departamento, pk=id)
    frm = DepartamentoForm(request.POST or None, instance=departamento)

    if frm.is_valid():
        frm.save()
        return redirect('departamentos')

    return render(request, 'Questao-1/Departamentos/form.html',{
        'nome' : 'Editar Departamentos',
        'frm':frm
    })

def excluir(request,id):

    departamento = get_object_or_404(Departamento, pk=id)
    departamento.delete()

    return redirect('departamentos')
from django.shortcuts import get_object_or_404, render, redirect
from Segundo_Trimestre.models import Corretor
from django.forms import ModelForm

class CorretorForm(ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'


def listar(request):

    corretors = Corretor.objects.all()

    return render(request, 'Questao-3/Corretor/listar.html',{
        "nome": "Lista de Corretores",
        "corretors": corretors
    })

def criar(request):

    frm = CorretorForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('corretores')

    return render(request, 'Questao-3/Corretor/form.html',{
        "nome":"Cadastro de Corretor",
        "frm": frm
    })

def editar(request, id):
    corretor = get_object_or_404(Corretor, pk=id)
    frm = CorretorForm(request.POST or None, instance=corretor)

    if frm.is_valid():
        frm.save()
        return redirect('corretores')

    return render(request,'Questao-3/corretor/form.html',{
        "nome":"Editar Corretor",
        "frm":frm
    })

def excluir(request, id):
    corretor = get_object_or_404(Corretor,pk=id)
    corretor.delete()

    return redirect('corretores')
from django.shortcuts import get_object_or_404, redirect, render
from Segundo_Trimestre.models import Habilitacao
from django.forms import ModelForm

class HabilitacaoForm(ModelForm):
    class Meta:
        model = Habilitacao
        fields = '__all__'

def listar(request):

    Habilitacoes = Habilitacao.objects.all()

    return render(request, 'Questao-2/Habilitação/listar.html',{
        'nome': 'Listar Habilitações',
        'habilitacoes': Habilitacoes
    })

def criar(request):
    
    frm = HabilitacaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('habilitacoes')

    return render(request, 'Questao-2/Habilitação/form.html',{
        'nome' : 'Cadastrar uma nova Habilitação',
        'frm' : frm
    })

def editar(request, id):
    
    habilitacao = get_object_or_404(Habilitacao, pk=id)
    frm = HabilitacaoForm(request.POST or None, instance=habilitacao)

    if frm.is_valid():
        frm.save()
        return redirect('habilitacoes')

    return render(request, 'Questao-2/Habilitação/form.html',{
        'nome' : 'Editar uma Habilitacao',
        'frm' : frm
    })

def excluir(request, id):
    
    habilitacao = get_object_or_404(Habilitacao, pk=id)
    habilitacao.delete()

    return redirect('habilitacoes')

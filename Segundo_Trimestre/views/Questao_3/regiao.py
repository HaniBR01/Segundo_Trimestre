from django.shortcuts import get_object_or_404, render, redirect
from Segundo_Trimestre.models import Regiao
from django.forms import ModelForm

class RegiaoForm(ModelForm):
    class Meta:
        model = Regiao
        fields = '__all__'

def listar(request):

    Regiaos = Regiao.objects.all()

    return render(request, 'Questao-3/Regiao/listar.html',{
       "nome": "Listar Regiões",
       "regiaos": Regiaos
    })

def criar(request):
    frm = RegiaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('regiaos')
    
    return render(request, 'Questao-3/Regiao/form.html',{
        "nome": "Cadastrar uma Região",
        "frm": frm
    })

def editar(request, id):
    regiao = get_object_or_404(Regiao, pk=id)
    frm = RegiaoForm(request.POST or None, instance=regiao)

    if frm.is_valid():
        frm.save()
        return redirect('regiaos')
    
    return render(request, 'Questao-3/Regiao/form.html',{
        "nome": "Editar a Região",
        "frm": frm
    })

def excluir(request, id):
    regiao = get_object_or_404(Regiao, pk=id)
    regiao.delete()

    return redirect('regiaos')
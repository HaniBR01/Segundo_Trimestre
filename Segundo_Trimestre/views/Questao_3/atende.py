from django.shortcuts import get_object_or_404, render, redirect
from Segundo_Trimestre.models import CorretorAtendeRegiao
from django.forms import ModelForm

class AtendeForm(ModelForm):
    class Meta:
        model = CorretorAtendeRegiao
        fields = '__all__'

def listar(request):

    Atendes = CorretorAtendeRegiao.objects.all()

    return render(request, 'Questao-3/Atende/listar.html',{
       "nome": "Listar os Atendimentos",
       "atendes": Atendes
    })

def criar(request):
    frm = AtendeForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('atendes')
    
    return render(request, 'Questao-3/Atende/form.html',{
        "nome": "Cadastrar um Atendimento",
        "frm": frm
    })

def editar(request, id):
    atende = get_object_or_404(CorretorAtendeRegiao, pk=id)
    frm = AtendeForm(request.POST or None, instance=atende)

    if frm.is_valid():
        frm.save()
        return redirect('atendes')
    
    return render(request, 'Questao-3/Atende/form.html',{
        "nome": "Editar o Atendimento",
        "frm": frm
    })

def excluir(request, id):
    atende = get_object_or_404(CorretorAtendeRegiao, pk=id)
    atende.delete()

    return redirect('atendes')
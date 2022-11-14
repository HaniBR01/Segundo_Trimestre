from django.shortcuts import get_object_or_404, render, redirect
from Segundo_Trimestre.models import Telefone
from django.forms import ModelForm

class TelefoneForm(ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'

def listar(request):

    Telefones = Telefone.objects.all()

    return render(request, 'Questao-3/Telefone/listar.html',{
       "nome": "Listar Telefones",
       "telefones": Telefones
    })

def criar(request):
    frm = TelefoneForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('telefones')
    
    return render(request, 'Questao-3/Telefone/form.html',{
        "nome": "Cadastrar um Telefone",
        "frm": frm
    })

def editar(request, id):
    telefone = get_object_or_404(Telefone, pk=id)
    frm = TelefoneForm(request.POST or None, instance=telefone)

    if frm.is_valid():
        frm.save()
        return redirect('telefones')
    
    return render(request, 'Questao-3/Telefone/form.html',{
        "nome": "Editar o Telefone",
        "frm": frm
    })

def excluir(request, id):
    telefone = get_object_or_404(Telefone, pk=id)
    telefone.delete()

    return redirect('telefones')
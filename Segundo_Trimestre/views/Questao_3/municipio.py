from django.shortcuts import get_object_or_404, render, redirect
from Segundo_Trimestre.models import Municipio
from django.forms import ModelForm

class MunicipioForm(ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__'

def listar(request):

    Municipios = Municipio.objects.all()

    return render(request, 'Questao-3/Municipio/listar.html',{
       "nome": "Listar Municipios",
       "municipios": Municipios
    })

def criar(request):
    frm = MunicipioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('municipios')
    
    return render(request, 'Questao-3/Municipio/form.html',{
        "nome": "Cadastrar um Município",
        "frm": frm
    })

def editar(request, id):
    municipio = get_object_or_404(Municipio, pk=id)
    frm = MunicipioForm(request.POST or None, instance=municipio)

    if frm.is_valid():
        frm.save()
        return redirect('municipios')
    
    return render(request, 'Questao-3/Municipio/form.html',{
        "nome": "Editar o Município",
        "frm": frm
    })

def excluir(request, id):
    municipio = get_object_or_404(Municipio, pk=id)
    municipio.delete()

    return redirect('municipios')
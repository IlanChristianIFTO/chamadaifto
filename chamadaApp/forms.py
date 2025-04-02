from django import forms
from chamadaApp.models import Categoria,Plano,Telefone,Cliente

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        filds = '__all__'
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        filds = '__all__'
class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        filds = '__all__'
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        filds = '__all__'
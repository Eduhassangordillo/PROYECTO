from django import forms

class BiciFormularioBase(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    
class CrearBiciFormulario(BiciFormularioBase):
    ...
    
class EditarBiciFormulario(BiciFormularioBase):
    ...
    
class BuscarBici(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    
    
    
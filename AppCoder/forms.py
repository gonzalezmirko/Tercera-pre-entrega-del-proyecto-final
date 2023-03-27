from django import forms

class CursoForm(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class ProfesoresForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=30)
class EntregableForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    fechaEntrega=forms.DateField()
    entregado=forms.BooleanField()
class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()


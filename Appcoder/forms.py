from django import forms


class RecreadorFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    nacimiento = forms.DateField()
    
   
    
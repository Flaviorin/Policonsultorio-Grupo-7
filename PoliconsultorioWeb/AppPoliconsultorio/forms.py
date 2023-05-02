from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="DNI del paciente:", max_length=5, required=True,
        widget=forms.TextInput(attrs={"class": "special", "id":"44"}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    horario = forms.CharField(label="horario", required=True)   
    profesional = forms.CharField(label="dia", required=True)
   
		
class BajaTurnoForm(forms.Form):
    nombre = forms.CharField(label="DNI del paciente:", max_length=5, required=True,
        widget=forms.TextInput(attrs={"class": "special", "id":"44"}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    horario = forms.CharField(label="horario", required=True)   
    profesional = forms.CharField(label="dia", required=True)
   
    
 
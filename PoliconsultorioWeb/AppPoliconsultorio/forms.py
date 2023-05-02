from django import forms

from .medicos import lista_medicos
from .especialidades import lista_especialidades
from .pacientes import lista_pacientes

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto:", max_length=5, required=True,
        widget=forms.TextInput(attrs={"class": "special", "id":"44"}))
    apellido = forms.CharField(label="Apellido de contacto", required=True)
    email = forms.EmailField(required=True)

class ConsultaMedicosForm(forms.Form):
    # Definir campos
    # nombre = forms.CharField(label="Nombre", required=True)
    # especialidad = forms.Select(label="Especialidad", required=False)
    #listado_especialidades = lista_especialidades()
    especialidad = forms.ChoiceField(choices=lista_especialidades(), required=True, widget=forms.Select)
    medico = forms.CharField(label="Médico", widget=forms.TextInput(attrs={'class': 'medico'}), required=False)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})),

class ConsultaTurnosForm(forms.Form):
    # Definir campos
    # nombre = forms.CharField(label="Nombre", required=True)
    # especialidad = forms.Select(label="Especialidad", required=False)
    # paciente = forms.ChoiceField(choices=lista_pacientes(), required=False, widget=forms.Select(attrs={"class": "form-control", "id":"paciente"}))
    paciente = forms.CharField(label="DNI Paciente", widget=forms.TextInput(attrs={'class': 'paciente'}), required=False)
    especialidad = forms.ChoiceField(label=' Especialidad', choices=lista_especialidades(), required=False, widget=forms.Select)
    # # medico = forms.CharField(label="Médico", widget=forms.TextInput(attrs={'class': 'medico'}), required=False)
    medico = forms.ChoiceField(label=' Médico', choices=lista_medicos(), required=False, widget=forms.Select)
    fecha_desde = forms.DateField(label=' Fecha Desde',widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_hasta = forms.DateField(label=' Fecha Hasta',widget=forms.DateInput(attrs={'type': 'date'}), required=False)

from django import forms
from django.forms.fields import DateField

from .especialidades import lista_especialidades
from .medicos import lista_medicos

class AltaTurnoForm(forms.Form):

#<<<<<<< HEAD
    listado_especialidad = lista_especialidades()
#=======
    listado_especialidad = (('Z','Seleccione una especialidad'),('Cardiología','Cardiología'),('Dermatología','Dermatología'),('Neurología','Neurología'),('Oftalmología','Oftalmología'),('Pediatría','Pediatría'))
#>>>>>>> 090f2d36a8ca3ddae2503497eb4b94947987ca8a

    listado_medicos = lista_medicos()

    paciente = forms.CharField(label="pacientex:", max_length=8, min_length=7 ,required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id":"paciente"}))
    especialidad = forms.ChoiceField(label="especialidadx:",required=False, choices = listado_especialidad,
        widget=forms.Select(attrs={"class": "form-control", "id":"especialidad"}))
    medico = forms.ChoiceField(label="medicox:", required=False, choices = listado_medicos,
        widget=forms.Select(attrs={"class": "form-control", "id":"medico"}))
    fecha = forms.DateField(label="fechax:",required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "id":"fecha",'type': 'date'}))

def lista_turnos():
    listado_turnos = [
        {
            'dia': '20/04/2023',
            'hora': '09:00',
            'medico': 'Dr. Juan Pérez',
            'especialidad': 'Cardiología',
            'paciente': 'Adriana Cullen',
        },
        {
            'dia': '20/04/2023',
            'hora': '09:00',
            'medico': 'Dra. María González',
            'especialidad': 'Dermatología',
            'paciente': 'José Olleros',
        },
        {
            'dia': '20/04/2023',
            'hora': '11:00',
            'medico': 'Dr. Juan Perez',
            'especialidad': 'Cardiología',
            'paciente': 'Mariano Burgos',
        },
    ]
    return listado_turnos

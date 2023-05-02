from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from .forms import *
from .turno import *

from .especialidades import lista_especialidades
from .medicos import lista_medicos

# Create your views here.
def index(request):
    
    # Listar todos los turnos del día
    turno = {
        'dia': '20/04/2023',
        'hora': '09:00',
        'medico': 'Dr. Juan Perez',
        'especialidad': 'Cardiología',
        'paciente': 'Adriana Cullen',
    }

    listado_turnos = lista_turnos()

    context = {
        "hoy": datetime.now,
        "dia": "18/04/2023",
        "turno": turno,
        "listado_turnos": listado_turnos,
        }
    return render(request, "AppPoliconsultorio/index.html", context)

def turno_medico(request):

    listado_especialidad = lista_especialidades()

    listado_medicos = lista_medicos()

    listado_disp_medicos = [{'ID':'1',
                             'horario':'8:00 a 9:00',
                             'descr_disponible':'Disponible',
                             'flag':'enabled',
                             },
                            {'ID':'2',
                            'horario':'9:00 a 10:00',
                            'descr_disponible':'No disponible',
                            'flag':'disabled',
                            },
                            {'ID':'3',
                             'horario':'10:00 a 11:00',
                             'descr_disponible':'Disponible',
                             'flag':'enabled',
                             }]

    context = {
        "listado_especialidad":listado_especialidad,
        "listado_medicos":listado_medicos,
        "listado_disp_medicos":listado_disp_medicos,
    }

    if request.method == "POST":
        # Creo la instancia del formulario con los datos cargados en pantalla
        alta_turno_form = AltaTurnoForm(request.POST)
        # Valido y proceso los datos.
        if alta_turno_form.is_valid():        
            print('Paciente: ',alta_turno_form.cleaned_data['paciente'])
            #print('Paciente: ',alta_turno_form.data['Juan carlos'])
            print('Especialidad: ',alta_turno_form.cleaned_data['especialidad'])
            print('Medico: ',alta_turno_form.cleaned_data['medico'])
            print('Fecha: ',alta_turno_form.cleaned_data['fecha'])
            #print('Horario: ',alta_turno_form.cleaned_data['horario'])
            #print('Disponible: ',alta_turno_form.cleaned_data['disponible'])
            #print('Flag_Disponible: ',alta_turno_form.cleaned_data['flag_disponible'])
            #Redirect to a new url:
            print("Es valido")
            return HttpResponseRedirect('/AppPoliconsultorio/turno_medico/')
    else:
        # Creo el formulario vacío con los valores por defecto
        alta_turno_form = AltaTurnoForm()
    return render(request, "AppPoliconsultorio/turnos.html", {'alta_turno_form': alta_turno_form})
    #return render(request,"AppPoliconsultorio/turnos.html",context)

def turno_consulta(request):
    listado_turnos = lista_turnos()
    
    if request.method == "POST":
        turno_consulta_form = ConsultaTurnosForm(request.POST)
        if turno_consulta_form.is_valid():
        #    if turno_consulta_form.is_bound():
            print(turno_consulta_form.cleaned_data['fecha_desde'])
            pass
        else:
            pass
    else:
        turno_consulta_form = ConsultaTurnosForm()

    context = {
        "listado_turnos": listado_turnos,
        "turno_consulta_form": turno_consulta_form,
    }
    return render(request, "AppPoliconsultorio/turno_consulta.html", context)

def especialidades(request):
    context = {}
    return render (request,"AppPoliconsultorio/especialidades.html", context)

def usuarios(request):
    context = {}
    return render (request,"AppPoliconsultorio/usuarios.html", context)


def contactenos(request):
    context = {}
    return render (request,"AppPoliconsultorio/contactenos.html", context)

def acerca(request):
    context = {}
    return render (request,"AppPoliconsultorio/acerca.html", context)

def contacto(request):
    if request.method == "POST":
    # Creo la instancia del formulario con los datos cargados en pantalla
        contacto_form = ContactoForm(request.POST)
        # Valido y proceso los datos.
        if contacto_form.is_valid():
            #Process the data in form.cleaned_data as required # ...
            # De esta manera veo los datos que fueron completados en el formulario
            print('Nombre: ',contacto_form.cleaned_data['nombre'])
            print('Apellido: ',contacto_form.cleaned_data['apellido'])
            print('Email: ',contacto_form.cleaned_data['email'])
            #Redirect to a new url:
            return HttpResponseRedirect('/AppPoliconsultorio/thanks/')
    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()
    return render(request, "AppPoliconsultorio/contacto.html", {'contacto_form': contacto_form})
    
def thanks(request): #new
    context = {}
    return render(request,"AppPoliconsultorio/thanks.html",context)

def consulta_medicos(request):
    # Prepara los combos
    listado_especialidad = lista_especialidades()
    listado_medicos = lista_medicos()

    if request.method == "POST":
        consulta_medicos_form = ConsultaMedicosForm(request.POST)
    else:
        consulta_medicos_form = ConsultaMedicosForm()

    context = {
        "listado_especialidad": listado_especialidad,
        "listado_medicos": listado_medicos,
        "form": consulta_medicos_form,
    }
    return render(request, "AppPoliconsultorio/consulta_medicos.html", context)

def alta_medico(request):
    # Alta de un Médico
    context = {}
    return render(request, "AppPoliconsultorio/alta_medico.html", context)

def baja_medico(request):
    # Baja de un Médico
    context = {}
    return render(request, "AppPoliconsultorio/baja_medico.html", context)

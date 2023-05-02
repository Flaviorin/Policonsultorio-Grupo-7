from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .turno import AltaTurnoForm
from .forms import *
from django.http import HttpResponseRedirect

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

    context = {
        "hoy": datetime.now,
        "dia": "18/04/2023",
        "turno": turno,
        "listado_turnos": listado_turnos,
        }
    return render(request, "AppPoliconsultorio/index.html", context)


# comento porque esta funcion esta definida justo aca arriba
""" def index(request):
    context = {}
    return render (request,"AppPoliconsultorio/index.html", context) """



def contacto(request):
    turnos_otorgados = [
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

    context = {
        'nombre': 'Juana',
        'turnos': turnos_otorgados,
   }
    
def baja_turno(request):
    turnos_otorgados = [
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

    context = {
        'nombre': 'Juana',
        'turnos': turnos_otorgados,
   }     
    if request.method == "POST":
        # Creo la instancia del formulario con los datos cargados en pantalla
        bajaturno_form = BajaTurnoForm(request.POST)
        # Valido y proceso los datos.
        
        if bajaturno_form.is_valid():              
           
            return render(request, "AppPoliconsultorio/baja_turno.html", context) 
             
    else:
            # Creo el formulario vacío con los valores por defecto
        bajaturno_form = BajaTurnoForm()
    return render(request, "AppPoliconsultorio/baja_turno.html", {'bajaturno_form': bajaturno_form })
    

   






def turno_medico(request):

    listado_especialidad = ['Cardiología','Dermatología',
        'Neurología','Oftalmología','Pediatría']

    listado_medicos = [{'ID':'1','nombre':'Dr. Juan Pérez (Cardiología)','Especialidad':'Cardiología'},
                       {'ID':'2','nombre':'Dra. María González (Dermatología)','Especialidad':'Dermatología'},
                       {'ID':'3','nombre':'Dr. Luis Sánchez (Neurología)','Especialidad':'Neurología'},
                       {'ID':'4','nombre':'Dra. Ana Rodríguez (Oftalmología)','Especialidad':'Oftalmología'},
                       {'ID':'5','nombre':'Dr. Pedro López (Pediatría)','Especialidad':'Pediatría'}
                       ]    

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
            print('Documento: ',contacto_form.cleaned_data['nombre'])
            
            # print('Apellido: ',contacto_form.cleaned_data['apellido'])
           
            #Redirect to a new url:
            # return HttpResponseRedirect('/AppPoliconsultorio/thanks/')
    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()
    return render(request, "AppPoliconsultorio/contacto.html", {'contacto_form': contacto_form})
    
def thanks(request): #new
    context = {}
    return render(request,"AppPoliconsultorio/thanks.html",context)    
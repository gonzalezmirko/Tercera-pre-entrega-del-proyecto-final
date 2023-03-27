from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.models import Profesor
from AppCoder.models import Estudiante
from AppCoder.models import Entregable
from AppCoder.forms import CursoForm
from AppCoder.forms import ProfesoresForm
from AppCoder.forms import EntregableForm
from AppCoder.forms import EstudianteForm

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def cursos(request):
 
      if request.method == "POST":
            miFormulario = CursoForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()
                return render(request, "AppCoder/cursos.html")
      else:
            miFormulario = CursoForm()
 
      return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def profesores(request):
 
      if request.method == "POST":
            miFormulario = ProfesoresForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],profesion=informacion["profesion"])
                  profesor.save()
                  return render(request, "AppCoder/profesores.html")
      else:
            miFormulario = ProfesoresForm()
 
      return render(request, "AppCoder/profesores.html", {"miFormulario": miFormulario})

def estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            estudiante.save()
            return render(request, "AppCoder/estudiantes.html")
    else:
        miFormulario = EstudianteForm()
 
    return render(request, "AppCoder/estudiantes.html", {"miFormulario": miFormulario})

def entregables(request):
    if request.method == "POST":
        miFormulario = EntregableForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"], fechaEntrega=informacion["fechaEntrega"],entregado=informacion["entregado"])
            entregable.save()
            return render(request, "AppCoder/entregables.html")
    else:
        miFormulario = EntregableForm()
 
    return render(request, "AppCoder/entregables.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request,"AppCoder/busquedaCamada.html")

def buscar(request):
    if(request.GET["camada"]):
        #respuesta= f"Estoy buscando la camada numero: {request.GET['camada']}"
        camada=request.GET['camada']
        cursos=Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html",{"cursos":cursos,"camada":camada})
    else:
        respuesta="No enviaste datos"
    return render(request,"AppCoder/resultadosBusqueda.html",{"respuesta":respuesta})

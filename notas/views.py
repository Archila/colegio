from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Pensum
from .models import Grado
from .models import Curso
from .forms import GradoForm
# Create your views here.

def inicio(request):
    return render(request, 'notas/index.html')

def nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'],seccion=formulario.cleaned_data['seccion'])
            for curso_id in request.POST.getlist('cursos'):
                pensum = Pensum(grado_id=grado.id, curso_id = curso_id)
                pensum.save()
            
    else:
        formulario = GradoForm()
    return render(request, 'notas/new.html', {'formulario': formulario})

def ver(request):
    pensums = Grado.objects.filter()
    return render(request, 'notas/show.html',{'pensums': pensums})

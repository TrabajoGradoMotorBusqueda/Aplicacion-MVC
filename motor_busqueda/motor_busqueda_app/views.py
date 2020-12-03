from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Docente, Estudiante
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("index")


########################    INVESTIGACION DOCENTE    #############################

# class InvestigacionDocenteCreateView(CreateView):
# 	model=Docente
# 	template_name='motor_busqueda_app/InvestigacionDocenteCreate.html'
# 	fields = ['id_investigacion']

class InvestigacionDocenteListView(ListView):
	model=Docente
	template_name='motor_busqueda_app/InvestigacionDocenteList.html'
	context_object_name = 'investigaciones_docentes'


class InvestigacionDocenteDetailView(DetailView):
	model=Docente
	template_name='motor_busqueda_app/InvestigacionDocenteDetail.html'
	context_object_name = 'investigacion_docente'


# class InvestigacionDocenteUpdateView(UpdateView):
# 	model=Docente
# 	template_name='motor_busqueda_app/InvestigacionDocenteUpdate.html'




########################     INVESTIGACION ESTUDIANTE    ########################

# class InvestigacionEstudianteCreateView(CreateView):
# 	model=Estudiante
# 	template_name='motor_busqueda_app/InvestigacionEstudianteCreate.html'
# 	fields = ['id_investigacion']


class InvestigacionEstudianteListView(ListView):
	model=Estudiante
	template_name='motor_busqueda_app/InvestigacionEstudianteList.html'
	context_object_name = 'investigaciones_estudiantes'


class InvestigacionEstudianteDetailView(DetailView):
	model=Estudiante
	template_name='motor_busqueda_app/InvestigacionEstudianteDetail.html'
	context_object_name = 'investigacion_estudiante'


# class InvestigacionEstudianteUpdateView(UpdateView):
# 	model=Estudiante
# 	template_name='motor_busqueda_app/InvestigacionEstudianteUpdate.html'



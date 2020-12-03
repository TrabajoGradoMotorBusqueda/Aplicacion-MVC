from django.urls import path

from motor_busqueda_app import views

urlpatterns = [
    path('', views.index, name='index'),

	path('investigacion_docente/',views.InvestigacionDocenteListView.as_view(), name=''),
	# path('investigacion_docente/crear/',views.InvestigacionDocenteCreateView.as_view(), name=''),
	# path('investigacion_docente/editar/{id}/',views.InvestigacionDocenteUpdateView.as_view(), name=''),
	path('investigacion_docente/visualizar/<int:pk>/',views.InvestigacionDocenteDetailView.as_view(), name=''), 
	path('investigacion_estudiante/',views.InvestigacionEstudianteListView.as_view(), name=''), 
	# path('investigacion_estudiante/crear/',views.InvestigacionEstudianteCreateView.as_view(), name=''), 
	# path('investigacion_estudiante/editar/{id}/',views.InvestigacionEstudianteUpdateView.as_view(), name=''), 
	path('investigacion_estudiante/visualizar/<int:pk>/',views.InvestigacionEstudianteDetailView.as_view(), name=''), 
]



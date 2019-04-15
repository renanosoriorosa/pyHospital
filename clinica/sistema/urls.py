from django.urls import path
from .views import (
    listaMedicos,
    cadastraMedico,
    editaMedico,
    deleteMedico,

    listaEspecialidades,
    cadastraEspecialidade,
    editaEspecialidade,

    listaPacientes,
    cadastraPaciente,
    editaPaciente,
    deletePaciente,
    listaConsultas,
    cadastraConsulta
)

urlpatterns = [
    path('', listaConsultas, name='lista_consultas'),

    path('consultas/', listaConsultas, name='lista_consultas'),
    path('cadastraconsulta/', cadastraConsulta, name='cadastra_consulta'),

    path('medicos/', listaMedicos, name='lista_medicos'),
    path('cadastramedico/', cadastraMedico, name='cadastra_medico'),
    path('editamedico/<int:id>/', editaMedico, name='edita_medico'),
    path('deletemedico/<int:id>/', deleteMedico, name='delete_medico'),

    path('especialidades/', listaEspecialidades, name='lista_especialidades'),
    path('cadastraespecialidades/', cadastraEspecialidade, 
        name='cadastra_especialidade'),
    path('editaespecialidade/<int:id>/', editaEspecialidade, 
        name='edita_especialidade'),
    
    path('pacientes/', listaPacientes, name='lista_pacientes'),
    path('cadastrapaciente/', cadastraPaciente, name='cadastra_paciente'),
    path('editapaciente/<int:id>/', editaPaciente, 
        name='edita_paciente'),
    path('deletepaciente/<int:id>/', deletePaciente, 
        name='delete_paciente'),
]
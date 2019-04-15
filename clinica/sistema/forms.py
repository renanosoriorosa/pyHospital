from django.forms import ModelForm
from .views import (
    Medico,
    Especialidade,
    Paciente,
    Consulta
)

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__' #todos os campos dos medicos

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__' #todos os campos dos medicos

class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = '__all__' #todos os campos dos medicos

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__' #todos os campos dos medicos
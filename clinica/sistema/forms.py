from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )


class CadastraUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
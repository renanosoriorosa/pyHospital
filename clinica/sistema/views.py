from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import(
    Medico,
    Especialidade,
    Paciente,
    Consulta
)
from .forms import (
    MedicoForm,
    EspecialidadeForm,
    PacienteForm,
    ConsultaForm,
	EditarPerfilForm,
	CadastraUsuarioForm
)
# Create your views here.
@login_required()
def listaConsultas(request):
    consultas = Consulta.objects.all()
    form = ConsultaForm()
    data = {'consultas':consultas , 'form':form}
    return render(request, 'sistema/consultas/lista-consultas.html', data)

@login_required()
def cadastraConsulta(request):
    form = ConsultaForm(request.POST or None)
    data = {'form':form}
    if form.is_valid():
        form.save()
        return redirect('lista_consultas')
    return render(request,'sistema/consultas/cadastraconsulta.html',data)


@login_required()
def editaConsulta(request, id):
	data = {}
	consulta = Consulta.objects.get(id=id) #pega a pessoa que vai se editada
	form = ConsultaForm(request.POST or None, instance = consulta) # inicia um formulario com os campos preenchidos
	data['consulta'] = consulta
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('lista_consultas')
	else:
		return render(request, 'sistema/consultas/editaconsulta.html', data)


@login_required()
def deleteConsulta(request, id):
	consulta = Consulta.objects.get(id=id)
	if request.method == 'POST':
		consulta.delete()
		return redirect('lista_consultas')
	else:
		return render(request, 'sistema/deleteconfirm.html', 
            {'obj': consulta, 'url': "/consultas/"})


#medicos
@login_required()
def listaMedicos(request):
    medicos = Medico.objects.all()
    form = MedicoForm()
    data = {'medicos':medicos , 'form':form}
    return render(request, 'sistema/medicos/lista-medicos.html', data)


@login_required()
def cadastraMedico(request):
    form = MedicoForm(request.POST or None)
    data = {'form':form}
    if form.is_valid():
        form.save()
        return redirect('lista_medicos')
    return render(request,'sistema/medicos/cadastramedico.html',data)


@login_required()
def editaMedico(request, id):
	data = {}
	medico = Medico.objects.get(id=id) #pega a pessoa que vai se editada
	form = MedicoForm(request.POST or None, instance = medico) # inicia um formulario com os campos preenchidos
	data['medico'] = medico
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('lista_medicos')
	else:
		return render(request, 'sistema/medicos/editamedico.html', data)


@login_required()
def deleteMedico(request, id):
	medico = Medico.objects.get(id=id)
	if request.method == 'POST':
		medico.delete()
		return redirect('lista_medicos')
	else:
		return render(request, 'sistema/deleteconfirm.html', 
            {'obj': medico, 'url': "/medicos/"})


@login_required()
def listaEspecialidades(request):
    especialidades = Especialidade.objects.all()
    form = EspecialidadeForm()
    data = {'especialidades':especialidades , 'form':form}
    return render(request, 
        'sistema/especialidade/lista-especialidades.html', data)


@login_required()
def cadastraEspecialidade(request):
	form = EspecialidadeForm(request.POST or None)
	data = {'form':form}
	if form.is_valid():
		form.save()
		return redirect('lista_especialidades')


@login_required()
def editaEspecialidade(request, id):
	if not request.user.has_perm('especialidade.change_especialidade'):
		return HttpResponse('Sem Permissão')
	data = {}
	especialidade = Especialidade.objects.get(id=id) #pega a pessoa que vai se editada
	form = EspecialidadeForm(request.POST or None, instance = especialidade) # inicia um formulario com os campos preenchidos
	data['especialidade'] = especialidade
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('lista_especialidades')
	else:
		return render(request, 'sistema/especialidade/editaespecialidade.html', data)


@login_required()
def deleteEspecialidade(request, id):
	especialidade = Especialidade.objects.get(id=id)
	if request.method == 'POST':
		especialidade.delete()
		return redirect('lista_especialidades')
	else:
		return render(request, 'sistema/deleteconfirm.html', 
            {'obj': especialidade, 'url': "/especialidades/"})


@login_required()
def listaPacientes(request):
    pacientes = Paciente.objects.all()
    form = PacienteForm()
    data = {'pacientes':pacientes , 'form':form}
    return render(request, 
        'sistema/pacientes/lista-pacientes.html', data)


@login_required()
def cadastraPaciente(request):
    form = PacienteForm(request.POST or None)
    data = {'form':form}
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request,'sistema/pacientes/cadastrapaciente.html',data)



@login_required()
def editaPaciente(request, id):
	data = {}
	paciente = Paciente.objects.get(id=id) #pega a pessoa que vai se editada
	form = PacienteForm(request.POST or None, instance = paciente) # inicia um formulario com os campos preenchidos
	data['paciente'] = paciente
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('lista_pacientes')
	else:
		return render(request, 'sistema/pacientes/editapaciente.html', data)


@login_required()
def deletePaciente(request, id):
	paciente = Paciente.objects.get(id=id)
	if request.method == 'POST':
		paciente.delete()
		return redirect('lista_pacientes')
	else:
		return render(request, 'sistema/deleteconfirm.html', 
            {'obj': paciente, 'url': "/pacientes/"})


#MEU PERFIL
@login_required()
def listaPerfil(request):
	args = {'user': request.user}
	return render(request, 'sistema/perfil/perfil.html', args)



@login_required()
def editaPerfil(request):
	if request.method == 'POST':
		form = EditarPerfilForm(request.POST, instance=request.user)
	
		if form.is_valid():
			form.save()
			return redirect('lista_perfil')
	
	else:
		form = EditarPerfilForm(instance=request.user)
		args = {'form': form}
		return render(request, 'sistema/perfil/editaperfil.html', args)


#cadastra usuario
@login_required()
def cadastraUsuario(request):
	if not request.user.has_perm('usuario.view_user'):
		return HttpResponse('Sem Permissão')
	if request.method == 'POST':
		form = CadastraUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cadastra_usuario_sucesso')
	else:
		form = CadastraUsuarioForm()
		args = {'form':form}
		return render(request, 'sistema/usuarios/cadastrausuario.html', args)


@login_required()
def cadastraUsuarioSucesso(request):
	return render(request, 'sistema/usuarios/cadastro-usuario-sucesso.html')

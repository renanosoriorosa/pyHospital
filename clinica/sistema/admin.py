from django.contrib import admin
from .models import (
    Medico,
    Especialidade,
    Paciente,
    Consulta
)

admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Paciente)
admin.site.register(Consulta)
# Register your models here.

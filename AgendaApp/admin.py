from django.contrib import admin
from AgendaApp.models import Agenda
from AgendaApp.models import Cidade
from AgendaApp.models import Telefone
# Register your models here.
admin.site.register(Agenda)
admin.site.register(Cidade)
admin.site.register(Telefone)
from django.contrib import admin
from AgendaApp.models import Agenda
from AgendaApp.models import Cidade
from AgendaApp.models import Telefone

# Register your models here.

class Telefones(admin.StackedInline):
    model = Telefone



class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'DataNascimento']
    list_filter = ['DataNascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]    



admin.site.register(Agenda, AgendaAdmin) 
admin.site.register(Cidade)
admin.site.register(Telefone)

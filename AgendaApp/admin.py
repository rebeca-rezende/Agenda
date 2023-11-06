from django.contrib import admin
from AgendaApp.models import Agenda
from AgendaApp.models import Cidade
from AgendaApp.models import Telefone
from AgendaApp.models import Interesse

# Register your models here.

class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'DataNascimento']
    list_filter = ['DataNascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]   
    filter_horizontal = ['interesses'] 


admin.site.register(Agenda, AgendaAdmin) 
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)

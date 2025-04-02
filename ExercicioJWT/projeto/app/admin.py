from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pessoa

class PessoaAdmin(UserAdmin):
    list_display = ['username','email','idade', 'telefone', 'endereco', 'escolaridade','numero_animais']
    fieldsets = UserAdmin.fieldsets +((None,{"fields":('idade', 'telefone', 'endereco', 'escolaridade','numero_animais')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields":('idade', 'telefone', 'endereco', 'escolaridade','numero_animais')}),)

admin.site.register(Pessoa, PessoaAdmin)
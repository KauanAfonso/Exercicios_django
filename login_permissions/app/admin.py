from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    #Quando eu for visializar um registro
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'apelido','telefone','genero', 'colaborador', 'empresa'
            ),
        }),
    )

    #quando for adicionar mais um registro
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'apelido','telefone','genero', 'colaborador', 'empresa'
            ),
        }),
    )
    

admin.site.register(models.Usuario, UsuarioAdmin)
admin.site.register(models.Empresa)
admin.site.register(models.Ingresso)
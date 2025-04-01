from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16, Pessoa
# Register your models here.
class UsuarioDS16Admin(UserAdmin):
    list_display = ('username', 'email', 'data_nascimento', 'edv', 'padrinho', 'apelido', 'pk')#definido os campos que aparecerá do usuário

    #Clicar no usuario especifico aparecer essas informações
    fieldsets = UserAdmin.fieldsets +(
        (None, {
            "fields": ( 
                'pk',
                'data_nascimento',
                'edv',
                'padrinho',
                'apelido',
                
            ),
        }),
    )
    
    #Quando for criar um usuário NOVO aparecer isso daqui
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {
            "fields": ( 
                'data_nascimento',
                'edv',
                'padrinho',
                'apelido'
            ),
        }),
    )

admin.site.register(UsuarioDS16,UsuarioDS16Admin)


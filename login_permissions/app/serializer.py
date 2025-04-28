from rest_framework import serializers
from .models import Usuario, Empresa
from rest_framework_simplejwt import TokenObtainPairSerializer #biblioteca para o django manipular o token e refresh

#--------------------------Serializando------------------
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = "__all__"

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    """
    Serializer responsável por validar e fornecer dados de autenticação para o login do usuário.
    Herda de TokenObtainPairSerializer para adicionar informações adicionais após a validação do token.
    """

    def validate(self, attrs):
        """
        Método responsável por validar as credenciais do usuário e retornar os dados do token junto com informações adicionais.
        
        Args:
            attrs (dict): Atributos enviados na requisição, como 'username' e 'password'.
        
        Returns:
            dict: Um dicionário contendo o token gerado e informações do usuário.
        """
        # Chama o método de validação da classe pai (TokenObtainPairSerializer)
        # O super().validate(attrs) retorna os dados do token gerado para o usuário.
        data = super().validate(attrs)
        
        # Adiciona um novo campo 'usuario' ao dicionário de dados retornado
        # Este campo contém o 'id' e 'username' do usuário autenticado
        data['usuario'] = {
            'id': self.user.id,  # ID do usuário autenticado
            'username': self.user.username  # Nome de usuário do usuário autenticado
        }

   
        return data

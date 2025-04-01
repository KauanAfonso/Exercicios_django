from .models import Pessoa

class PessaoSerializer(serializers.Serializer):
    class meta:
        model = Pessoa
        fields = "__all__"

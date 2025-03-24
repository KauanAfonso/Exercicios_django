from django import forms
from.models import livros


#Definie como será o formulario de item 
class itemForm(forms.ModelForm):
    class Meta:
        model = livros
        fields = ['titulo', 'autor', 'data_de_publicacao']
        widgets = {
            'data_de_publicacao': forms.DateInput(attrs={'type': 'date'}) #Aqui ele vai transformar meu input de text em de data
        }
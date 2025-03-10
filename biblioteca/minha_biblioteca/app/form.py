from django import forms
from.models import livros

class itemForm(forms.ModelForm):
    class Meta:
        model = livros
        fields = ['titulo', 'autor', 'data_de_publicacao']
        widgets = {
            'data_de_publicacao': forms.DateInput(attrs={'type': 'date'})
        }
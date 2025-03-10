from django import forms
from.models import livros

class itemForm(forms.ModelForm):
    class Meta:
        model = livros
        fields = "__all__"
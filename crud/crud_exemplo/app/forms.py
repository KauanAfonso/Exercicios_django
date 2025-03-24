from django import forms
from .models import Item

#base do formulario que tratará os items
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
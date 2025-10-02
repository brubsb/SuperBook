from django import forms
from .models import Vilao

class VilaoForm(forms.ModelForm):
    class Meta:
        model = Vilao
        fields = ["codinome", "nome_real", "poder_principal", "cidade", "historia"]
        widgets = {
            "historia": forms.Textarea(attrs={"rows": 5}),
        }


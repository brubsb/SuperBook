from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control', # Classe principal do Bootstrap
                'placeholder': 'No que você está pensando?',
                'rows': 4
            }),
        }

    # Este método é chamado para limpar e validar os dados.
    # Podemos usá-lo para adicionar a classe de erro dinamicamente.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se o formulário foi submetido e tem erros...
        if self.errors:
            for field_name in self.errors:
                # Adiciona a classe 'is-invalid' ao widget do campo com erro
                self.fields[field_name].widget.attrs.update({'class': 'form-control is-invalid'})

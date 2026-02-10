from django import forms
from .models import usuario
from .models import mensagem

class MensagemForm(forms.ModelForm):
    class meta:
        model = mensagem
        fields = ['Nome',
                  "mensagem",]
        

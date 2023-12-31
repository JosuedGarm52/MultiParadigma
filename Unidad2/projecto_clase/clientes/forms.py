from django import ModelForm,EmailInput
from clientes.models import Cliente 

class clienteForm(ModelForm):
    class Meta:
        model  = Cliente
        fields = "__all__"
        widget :{
            "email":EmailInput(
                attrs={
                    'type':'email',
                    'class':'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }
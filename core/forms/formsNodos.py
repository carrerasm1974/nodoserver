from django import forms
from ..modelos.modelsnodo import *


class NodoEditarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NodoEditarForm, self).__init__(*args, **kwargs)
        self.fields['grupo'].widget.attrs = {
            'class': 'form-control',
            'style': 'min-width: 550px;',
            }
        self.fields['model'].widget.attrs = {'class': 'form-control'}
  
        
    class Meta:
        model = ClaseNodo
        fields = ['grupo','model']


class NodoCrearForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NodoCrearForm, self).__init__(*args, **kwargs)
        self.fields['grupo'].widget.attrs = {'class': 'form-control'}
        self.fields['model'].widget.attrs = {'class': 'form-control'}
        self.fields['llave'].widget.attrs = {'class': 'form-control'}  
        self.fields['color'].widget.attrs = {'class': 'form-control'}  
  

    class Meta:
        model = ClaseNodo
        fields = ['llave','grupo','model', 'color']

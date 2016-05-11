from django import forms
from models import PDF

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

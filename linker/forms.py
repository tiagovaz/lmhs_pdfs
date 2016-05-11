from django import forms
from models import PDF

class DocumentForm(forms.ModelForm):
    docfile = forms.FileField(label='Select a file')

    class Meta:
        model = PDF
        fields = ['docfile']

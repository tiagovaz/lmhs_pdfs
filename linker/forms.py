#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from models import PDF

class DocumentForm(forms.ModelForm):
    docfile = forms.FileField(label='Sélectionnez le fichier PDF')

    class Meta:
        model = PDF
        fields = ['docfile']

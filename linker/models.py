from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class PDF(models.Model):
    notice = models.CharField("Notice", max_length=150)
    pdf_name = models.CharField("Nom du Fichier PDF", max_length=150)
    found = models.CharField("Disponible", max_length=150)
    last_check = models.CharField("Date de verification", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "PDF"
        verbose_name_plural = "PDFs"
#        db_table = 'PDF'

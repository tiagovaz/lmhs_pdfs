#!/usr/bin/python
# -*- coding: utf-8 -*-

import django_tables2 as tables
from models import PDF

class PDFTable(tables.Table):
    notice = tables.TemplateColumn('<a href="JavaScript:newPopup(\'http://acaia.ca:8002/details/?notice_id={{ record.notice }}\');">{{ record.notice }}</a>', verbose_name='Document')
    pdf_filename = tables.TemplateColumn('<a href="http://oicrm.org/wp-content/rechercheBDlmhs/PDF/public/{{ record.pdf_name }}">{{ record.pdf_name }}</a>', verbose_name='Lien PDF')
    last_check = tables.Column(verbose_name='Dernière vérification')
    fix = tables.TemplateColumn('<a href="JavaScript:newPopup(\'/linker/list/?notice={{ record.notice }}\');"> Ajouter </a>', verbose_name='Ajouter PDF')

    class Meta:
        model = PDF
        fields = ('id', 'notice', 'projet', 'pdf_filename', 'last_check', 'fix')
        attrs = {"class": "paleblue"}

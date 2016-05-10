from django.shortcuts import render
from django_tables2   import RequestConfig
from django.views.generic import View
from tables import PDFTable
from models import PDF

class List(View):
    def get(self, request):
        data = PDF.objects.filter(found__contains='0')
        other_data = data.count()
        data_table = PDFTable(data)
        data_table.paginate(page=request.GET.get('page', 1), per_page=25)
        RequestConfig(request).configure(data_table)
        return render(request, 'list.html', {'table': data_table, 'other_data' : other_data})

    def post(self, request):
        pass

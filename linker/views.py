from django.shortcuts import render, render_to_response
from django_tables2   import RequestConfig
from django.views.generic import View
from tables import PDFTable
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import PDF, Document
from forms import DocumentForm

class ListAll(View):
    def get(self, request):
        data = PDF.objects.filter(found__contains='0')
        other_data = data.count()
        data_table = PDFTable(data)
        data_table.paginate(page=request.GET.get('page', 1), per_page=25)
        RequestConfig(request).configure(data_table)
        return render(request, 'list.html', {'table': data_table, 'other_data' : other_data})

    def post(self, request):
        pass

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('linker.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

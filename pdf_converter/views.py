from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from products import products

from FoodApp.models import food

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.
def show_products(request):
    products = food.objects.all()

    context = {
        "products": products
    }

    return render(request, 'pdf_converter/showInfo.html', context)

def pdf_report(reqquest):
    products = food.objects.all()

    template_path = 'pdf_converter/pdfReport.html'
    context = {'products': products}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = '"filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response,)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
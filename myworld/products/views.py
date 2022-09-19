from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products


def index(request):
    product = Products.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))

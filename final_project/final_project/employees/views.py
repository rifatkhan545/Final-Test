from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Employee



def index(request):
    employees = Employee.objects.all()
    template = loader.get_template('index.html')
    context = {'employees': employees}
    return HttpResponse(template.render(context, request))

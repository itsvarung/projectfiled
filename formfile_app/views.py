from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, FormView, UpdateView
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from formfile_app.forms import PersonBasictForm
from .models import  Person

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PersonBasicDetailsFormView(FormView):
    model = Person
    form_class = PersonBasictForm
    template_name = 'person_basic_details_form_view.html'

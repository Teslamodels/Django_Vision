from django.shortcuts import render
from django.views.generic import CreateView
from .forms import Create
from django.urls import reverse_lazy

class Signin(CreateView):
    form_class = Create
    success_url = reverse_lazy('home')
    template_name = 'registration/signin.html'
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class Articlehome(ListView):
    model = Article
    template_name = 'a_home.html'

class Detail(DetailView):
    model = Article
    template_name = 'a_detail.html'

class Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'a_update.html'
    fields = ['title', 'summary', 'body', 'photo']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'a_delete.html'
    success_url = reverse_lazy('article')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class Create(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'a_create.html'
    fields = ['title', 'summary', 'body', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


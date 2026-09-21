from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from.models import Technical
from django.views.generic import TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class TechnicalListViews(ListView):
    queryset = Technical.objects.all()
    template_name = 'list_texnika.html'
    context_object_name = 'texnika'

class TechnicalCreateViews(CreateView):
    model = Technical
    fields = ['name','desc','price']
    template_name = 'create_texnika.html'
    success_url = reverse_lazy('list')

class TechnicalDetailViews(DetailView):
    model = Technical 
    template_name = 'detail_texnika.html'
    context_object_name = 'texnika'


class TechnicalDeleteViews(DeleteView):
    model = Technical
    template_name = 'delete_texnika.html'
    success_url = reverse_lazy('list') 


class TechnicalUpdateViews(UpdateView):
    model = Technical
    fields = ['name', 'desc', 'price']
    template_name = 'update_texnika.html'
    success_url = reverse_lazy('list') 




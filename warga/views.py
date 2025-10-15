from django.shortcuts import render
from .models import Warga
from django.views.generic import ListView, DetailView

# Create your views here.
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'
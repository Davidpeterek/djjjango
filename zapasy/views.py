from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Hrac, Zapas, Klub


def index(request):
    context = {
        'nadpis': 'Fotbal',
        'fotbaliste': Hrac.objects.order_by('-narozeni')[:4]
    }
    return render(request, 'index.html', context=context)


def klub_detail(request, klub_id):
    klub = Klub.objects.get(id=klub_id)
    return render(request, 'kluby/detail.html', {'klub': klub})

def klub_list(request):
    kluby = Klub.objects.all()
    return render(request, 'kluby/list.html', {'kluby': kluby})

def zapas_detail(request, zapas_id):
    zapas = Zapas.objects.get(id=zapas_id)
    return render(request, 'zapas/zapas_detail.html', {'zapas': zapas})

def zapas_list(request):
    zapas = Zapas.objects.all()
    return render(request, 'zapas/zapas_list.html', {'zapasy': zapas})

def hrac_detail(request, hrac_id):
    hrac = Hrac.objects.get(id=hrac_id)
    return render(request, 'hrac/hrac_detail.html', {'hrac': hrac})

def hrac_list(request):
    hraci = Hrac.objects.all()
    return render(request, 'hrac/hrac_list.html', {'hraci': hraci})
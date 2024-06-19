from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('klub/<int:klub_id>/', views.klub_detail, name='detail.html'),
    path('kluby/', views.klub_list, name='list.html'),
    path('zapas/<int:zapas_id>/', views.zapas_detail, name='zapas_detail.html'),
    path('zapasy/', views.zapas_list, name='zapas_list.html'),
    path('hrac/<int:hrac_id>/', views.hrac_detail, name='hrac_detail.html'),
    path('hraci/', views.hrac_list, name='hrac_list.html'),
]
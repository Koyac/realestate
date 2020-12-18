from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index'),
    path('index/', views.index1, name='index'),
    path('work/', views.work, name='work'),
    path('contact/', views.contact, name='contact'),
]
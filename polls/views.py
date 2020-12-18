from django.shortcuts import render
from django.db import models
from .models import HPmodel


# Create your views here.
def index1(request):
    return render(request, 'index.html')

def work(request):
    return render(request, 'works.html')

def contact(request):
    return render(request, 'contact.html')
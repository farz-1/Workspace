from tkinter import ANCHOR
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': 'Farzwan Mohamed'}
    return render(request, 'rango/about.html', context=context_dict)

# Create your views here.

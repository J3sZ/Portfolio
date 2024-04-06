from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here


def ProjectListView(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{'projects' : projects })


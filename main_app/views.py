from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Finch, Nest

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'habitat', 'food', 'nesting', 'behavior', 'conservation']
class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches/"

class NestList(ListView):
    model = Nest
    template_name = 'nests/index.html'
class NestCreate(CreateView):
    model = Nest
    fields = "__all__"
    success_url = "/nests/"
class NestUpdate(UpdateView):
    model = Nest
    fields = '__all__'
class NestDelete(DeleteView):
    model = Nest
    success_url = "/nests/"
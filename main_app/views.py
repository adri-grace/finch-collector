from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Finch, Nest
from .forms import SitingForm

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
    siting_form = SitingForm()
    return render(request, 'finches/detail.html', 
        {
            'finch': finch,
            'siting_form': siting_form
        }
    )
def add_siting(request, finch_id):
    form = SitingForm(request.POST)
    if form.is_valid():
        new_siting = form.save(commit=False)
        new_siting.finch_id = finch_id
        new_siting.save()
    return redirect('detail', finch_id=finch_id)
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
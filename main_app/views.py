from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Finch, Nest, Similar
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
    # similars = Similar.objects.all()
    not_associated = Similar.objects.exclude(id__in=finch.similar.all().values_list('id'))
    siting_form = SitingForm()
    return render(request, 'finches/detail.html', 
        {
            'finch': finch,
            'siting_form': siting_form,
            'similars': not_associated
        }
    )
def add_siting(request, finch_id):
    form = SitingForm(request.POST)
    if form.is_valid():
        new_siting = form.save(commit=False)
        new_siting.finch_id = finch_id
        new_siting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_finch(request, finch_id, similar_id):
    Finch.objects.get(id=finch_id).similar.add(similar_id)
    return redirect('detail', finch_id=finch_id)
def disassoc_finch(request, finch_id, similar_id):
    Finch.objects.get(id=finch_id).similar.remove(similar_id)
    return redirect('detail', finch_id=finch_id)
class FinchCreate(CreateView):
    model = Finch
    fields = ['variety', 'color', 'habitat', 'food', 'nesting', 'behavior', 'conservation']
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
    fields = "__all__"
class NestDelete(DeleteView):
    model = Nest
    success_url = "/nests/"

class SimilarCreate(CreateView):
    model = Similar
    fields = "__all__"
    success_url = "/finches/"
class SimilarUpdate(UpdateView):
    model = Similar
    fields = "__all__"
    success_url = "/finches/"
class SimilarDelete(DeleteView):
    model = Similar
    success_url = "/finches/"
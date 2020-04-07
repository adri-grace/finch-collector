from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Finch, Nest, Similar, Photo
from .forms import SitingForm

import boto3
import uuid

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'finchcollector-ag'


# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            rror_message = 'Invalid sign up; try again.'

    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

@login_required
def finches_index(request):
    # finches = Finch.objects.all()
    finches = Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html', {'finches': finches})

@login_required
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

@login_required
def add_siting(request, finch_id):
    form = SitingForm(request.POST)
    if form.is_valid():
        new_siting = form.save(commit=False)
        new_siting.finch_id = finch_id
        new_siting.save()
    return redirect('detail', finch_id=finch_id)

@login_required
def assoc_finch(request, finch_id, similar_id):
    Finch.objects.get(id=finch_id).similar.add(similar_id)
    return redirect('detail', finch_id=finch_id)

@login_required
def disassoc_finch(request, finch_id, similar_id):
    Finch.objects.get(id=finch_id).similar.remove(similar_id)
    return redirect('detail', finch_id=finch_id)

@login_required
def add_photo(request, finch_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        # s3 = boto3.session.Session(profile_name='finchcollector').client('s3')
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, finch_id=finch_id)
            photo.save()
        except:
            print('An file error occurred in upload')
    return redirect('detail', finch_id=finch_id)

class FinchCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = ['variety', 'color', 'habitat', 'food', 'nesting', 'behavior', 'conservation']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class FinchUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = ['color', 'habitat', 'food', 'nesting', 'behavior', 'conservation']
class FinchDelete(LoginRequiredMixin, DeleteView):
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

class SimilarCreate(LoginRequiredMixin, CreateView):
    model = Similar
    fields = "__all__"
    success_url = "/finches/"
class SimilarUpdate(LoginRequiredMixin, UpdateView):
    model = Similar
    fields = "__all__"
    success_url = "/finches/"
class SimilarDelete(LoginRequiredMixin, DeleteView):
    model = Similar
    success_url = "/finches/"
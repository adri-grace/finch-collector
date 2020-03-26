from django.shortcuts import render
from django.http import HttpResponse

class Finch:
    def __init__(self, variety, color, sex, location):
        self.variety = variety
        self.color = color
        self.sex = sex
        self.location = location

finches = [
    Finch('House Finch', 'red with orange chest', 'male', 'Walnut Reservoir' ),
    Finch('Lesser Goldfinch', 'yellow, red, and grey', 'female', 'Yorba Regional Park'),
    Finch('Western Tanager', 'yellow and black', 'male', 'Irvine')
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Finch Collector</h1>')
def about(request):
    return render(request, 'about.html')
def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
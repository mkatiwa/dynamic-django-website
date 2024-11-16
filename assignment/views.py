from django.shortcuts import render
from .models import Team
from .models import Testimonials
# Create your views here.

def home(request):
    teams = Team.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, 'index.html', {'teams': teams, 'testimonials': testimonials})


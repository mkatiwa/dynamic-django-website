from django.shortcuts import render
from .models import Team
from .models import Testimonials
from .serializers import TeamSerializer
from rest_framework import viewsets

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

def home(request):
    teams = Team.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, 'index.html', {'teams': teams, 'testimonials': testimonials})

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = product.objects.filter(name__icontains=query)
        return render(request, 'results.html', {'results': results, 'query': query})
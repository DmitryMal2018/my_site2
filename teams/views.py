from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import render
from .models import Team


def HomeTeamsView(request):
    teams = Team.objects.all()
    return render(request,
                  'home.html',
                  {'teams': teams})


class HomePageView(ListView):
    model = Team
    template_name = 'home.html'
    context_object_name = 'all_teams_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'

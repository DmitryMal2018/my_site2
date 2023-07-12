from django.urls import path
from .views import HomeTeamsView, HomePageView, AboutPageView


urlpatterns = [
    path('', HomeTeamsView),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]

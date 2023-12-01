from django.urls import path

from .views import HomePageView, AboutPageView, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('search/', SearchResultsView.as_view(), name='search'),
]
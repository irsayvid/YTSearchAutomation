from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetchresults/<page>/', views.fetchstored, name='fetchstored'),
    path('fetchresults/', views.fetchstored, name='fetchstored'),
]
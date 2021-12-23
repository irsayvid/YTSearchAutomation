from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetchresults/<str:query>/<int:page>/', views.fetchstored, name='fetchstored'),
    path('fetchresults/<str:query>/', views.fetchstored, name='fetchstored'),
    path('fetchresults/<int:page>/', views.fetchstored, name='fetchstored'),
    path('fetchresults/', views.fetchstored, name='fetchstored'),
]
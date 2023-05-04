from django.urls import path
from .views import searchView, resultView

urlpatterns = [
    path('', searchView, name='search-view'),
    path('result/', resultView, name='result-view'),
]

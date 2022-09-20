from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('casas/',views.casas),
    path('autos/',views.autos),
]

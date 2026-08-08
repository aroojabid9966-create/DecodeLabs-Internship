from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.all_pet, name='all_pet'),
]
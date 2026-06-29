from django.urls import path
from . import views

urlpatterns = [
    path('bestseller/', views.bestseller_view, name='bestseller'),
]

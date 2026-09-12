from django.urls import path
from . import views 

urlpatterns = [
    path('tailwind_components', views.componets_view, name='tailwind_showcase'),
    path('alpinejs_vs_vanilaJS', views.javascrip_view, name='alpine_showcase'),
]
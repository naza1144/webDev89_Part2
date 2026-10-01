from django.urls import path
from . import views 

urlpatterns = [
    path('tailwind_components', views.componets_view, name='tailwind_showcase'),
    path('alpinejs_vs_vanilaJS', views.javascrip_view, name='alpine_showcase'),
    path('htmx_showcase', views.htmx_demo_view, name='htmx_showcase'),
    path('htmx_showcase/search', views.demo_search_view, name='demo_search_view'),
    path('htmx_showcase/items/add', views.htmx_item_add_view, name='htmx_showcase_add'),
    path('htmx_showcase/items/<int:pk>/edit', views.htmx_item_edit_view, name='htmx_showcase_edit'),
    path('htmx_showcase/items/<int:pk>/cancel', views.htmx_item_cancel_view, name='htmx_showcase_cancel'),
    path('htmx_showcase/items/<int:pk>/delete', views.htmx_item_delete_view, name='htmx_showcase_delete'),
]
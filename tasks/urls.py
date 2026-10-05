from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('filter/', views.task_filter_view, name='task_filter'),
    path('load-more/', views.task_load_more_view, name='task_load_more'),
    path('add/', views.task_add_view, name='task_add'),
    path('<int:pk>/toggle/', views.task_toggle_view, name='task_toggle'),
    path('<int:pk>/edit/form/', views.task_edit_form_view, name='task_edit_form'),
    path('<int:pk>/edit/', views.task_edit_view, name='task_edit'),
    path('<int:pk>/cancel/', views.task_cancel_view, name='task_cancel'),
    path('<int:pk>/delete/', views.task_delete_view, name='task_delete'),
]

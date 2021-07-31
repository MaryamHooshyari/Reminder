from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView,\
    CategoryListView, CategoryCreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('admin/', admin.site.urls, name='admin'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit', TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('addTask/', TaskCreateView.as_view(), name='add_task'),
    path('addCategory/', CategoryCreateView.as_view(), name='add_category'),
]

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Task, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TaskCreateForm, TaskUpdateForm


class TaskListView(ListView):
    """to show all tasks (in html I used template tag to remove overdue tasks)"""
    model = Task
    template_name = 'todo/task_list.html'


class TaskDetailView(DetailView):
    """to show any task's details"""
    model = Task
    template_name = 'todo/task_detail.html'


class TaskCreateView(CreateView):
    """to make a new task"""
    form_class = TaskCreateForm
    model = Task
    template_name = 'todo/add_task.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    """to edit a task"""
    form_class = TaskUpdateForm
    model = Task
    template_name = 'todo/task_edit.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    """to delete a task"""
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryListView(ListView):
    """to show all categories"""
    model = Category
    context = {'data': Task.objects.no_task()}
    template_name = 'todo/category_list.html'


class CategoryDetailView(DetailView):
    """to show any category's detail"""
    model = Category
    template_name = 'todo/category_detail.html'


class CategoryCreateView(CreateView):
    """to make a new category"""
    model = Category
    template_name = 'todo/add_category.html'
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    """to edit a category"""
    model = Category
    template_name = 'todo/category_edit.html'
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    """to delete a category"""
    model = Category
    template_name = 'todo/category_delete.html'
    success_url = reverse_lazy('category_list')


class OverdueTaskList(ListView):
    """to show all overdue tasks"""
    model = Task
    queryset = Task.objects.overdue_task()
    template_name = 'todo/overdue_list.html'

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Task, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TaskCreateForm, TaskUpdateForm


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class TaskCreateView(CreateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'todo/add_task.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    form_class = TaskUpdateForm
    model = Task
    template_name = 'todo/task_edit.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'todo/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'todo/category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'todo/add_category.html'
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'todo/category_edit.html'
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'todo/category_delete.html'
    success_url = reverse_lazy('category_list')

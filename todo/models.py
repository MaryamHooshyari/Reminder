from django.db import models
from django.db.models import Count
from django.urls import reverse
from datetime import datetime
import pytz


class TaskManager(models.Manager):
    def overdue_task(self):
        return self.filter(due_date__lt=datetime.now(pytz.timezone('Asia/Tehran')))

    def no_task(self):
        tasks = self.all()
        used_cats = []
        for task in tasks:
            used_cats.append(task.category)
        set(used_cats)
        cats = Category.objects.all()
        result = []
        for cat in cats:
            if cat not in used_cats:
                result.append(cat)
        return result


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        ordering = ['due_date']

    PRIORITY_CHOICES = [('1', 'important & urgent'),
                        ('2', 'important but not urgent'),
                        ('3', 'not important but urgent'),
                        ('4', 'not important & not urgent')]

    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300, blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES, default='1')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tasks')
    # 0: in progress & 1: done
    status = models.CharField(max_length=1, default='0')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = TaskManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def done(self):
        self.status = '1'

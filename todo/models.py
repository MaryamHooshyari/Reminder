from django.db import models


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
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

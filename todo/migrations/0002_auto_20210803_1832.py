# Generated by Django 3.2.5 on 2021-08-03 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='todo.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('1', 'important & urgent'), ('2', 'important but not urgent'), ('3', 'not important but urgent'), ('4', 'not important & not urgent')], default='1', max_length=5),
        ),
    ]

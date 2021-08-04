from django.core import serializers
from .models import Task
from django.http import HttpResponse
from django.template import loader
from Reminder.settings import BASE_DIR


def json_download(request):
    objects = Task.objects.all()
    with open(str(BASE_DIR) + '/tasks.json', "w") as out:
        mast_point = serializers.serialize("json", objects)
        out.write(mast_point)
    template = loader.get_template('todo/tasks_dl.html')
    context = {'object': objects}
    return HttpResponse(template.render(context, request))

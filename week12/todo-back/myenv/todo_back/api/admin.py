from django.contrib import admin
from api.models import TaskList,Task
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskList)



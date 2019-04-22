from django.shortcuts import render
from django.http import HttpResponse
from api.models import TaskList, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        t_lists = TaskList.objects.all()
        serializer = TaskListSerializer(t_lists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def task_list_num(request, num):
    try:
        task_list = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error: str(e)'}, safe=False)
    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(instance=task_list, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

def task(request, num):
    try:
        tasklist = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error: str(e)'}, safe=False)
    t = tasklist.task_set.all()
    serializer = TaskSerializer(t, many=True)
    return JsonResponse(serializer.data, safe=False)
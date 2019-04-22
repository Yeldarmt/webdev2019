from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST'])
def task_lists(request):
    if request.method == 'GET':
        t_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(t_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','DELETE'])
def task_list_num(request, num):
    try:
        task = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskListSerializer2(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def task(request, num):
    try:
        tasklist = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        tasks = tasklist.task_set.all()
        serializer = TaskSerializer2(tasks, many=True)
        return Response(serializer.data)





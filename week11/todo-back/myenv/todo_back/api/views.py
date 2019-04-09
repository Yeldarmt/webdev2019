from django.shortcuts import render
from api.models import TaskList
from django.http import JsonResponse,HttpResponse

def task_list(request):
    tasks = TaskList.objects.all()
    t_lists = [t.to_json() for t in tasks]
    return JsonResponse(t_lists, safe=False)

def task_list_num(request, num):
    try:
        task = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(task.to_json(), safe=False)
def task_list_num_task(request, num):
    try:
        task = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    t = task.task_set.all()
    json_t = [p.to_json() for p in t]
    return JsonResponse(json_t, safe=False)



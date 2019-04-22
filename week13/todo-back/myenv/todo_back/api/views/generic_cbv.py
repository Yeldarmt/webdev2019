from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer2, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class TaskListt(generics.ListCreateAPIView):
    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskList_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

#class Task(generics.ListAPIView):
    # task_list = TaskList.objects.get(id=pk)
    # tasks = task_list.task_set.all()
    # queryset = tasks
    # serializer_class = TaskSerializer2

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
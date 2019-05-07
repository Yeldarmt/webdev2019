from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer2, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import TaskFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


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

class TaskList_detail_task(generics.ListAPIView):
    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs.get('pk'))
        except:
            return Http404
        tasks = task_list.task_set.all()
        return tasks
    serializer_class = Task

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskListTasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer2
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # DjangoFilterBackend
    filter_class = TaskFilter
    #filterset_fields = ('name', 'status')

    #searchFilter
    search_fields = ('name', 'status')

    #OrderingFilter
    ordering_fields = ('name', 'status')
    ordering = ('-id', )
    def get_queryset(self):
        try:
            tasklist = TaskList.objects.get(id=self.kwargs.get('pk'))
        except TaskList.DoesNotExist:
            raise Http404

        queryset = tasklist.tasks.all()
        # #query params
        # name = self.request.query_params.get('name', None)
        # id = self.request.query_params.get('id', None)
        # if name is not None and id is not None:
        #     queryset = queryset.filter(name=name).filter(id=id)
        return queryset

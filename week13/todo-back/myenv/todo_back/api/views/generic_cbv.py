from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer2, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

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

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# from rest_framework import generics
# from api.models import Gym, Client, Test, Subscription
# from api.serializers import TestSerializer, SubscriptionSerializer
# from django.http import Http404
#
# class ShowTest(generics.ListCreateAPIView):
#     def get_queryset(self):
#         try:
#             gym = Gym.objects.get(id=self.kwargs.get('pk'))
#         except Gym.DoesNotExist:
#             raise Http404
#         try:
#             client = gym.client_set.get(id=self.kwargs.get('pk2'))
#         except Client.DoesNotExist:
#             raise Http404
#         try:
#             test = client.test_set.all()
#             return test
#         except Test.DoesNotExist:
#             raise Http404
#
#     serializer_class = TestSerializer
#
#
# class ShowSubscription(generics.ListCreateAPIView):
#     def get_queryset(self):
#         try:
#             gym = Gym.objects.get(id=self.kwargs.get('pk'))
#         except Gym.DoesNotExist:
#             raise Http404
#         try:
#             client = gym.client_set.get(id=self.kwargs.get('pk2'))
#         except Client.DoesNotExist:
#             raise Http404
#         try:
#             subscription = client.subscription_set.all()
#             return subscription
#         except Subscription.DoesNotExist:
#             raise Http404
#     serializer_class = SubscriptionSerializer
#
#
# class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
#     def get_queryset(self):
#         try:
#             gym = Gym.objects.get(id=self.kwargs.get('pk'))
#         except Gym.DoesNotExist:
#             raise Http404
#         try:
#             client = gym.client_set.get(id=self.kwargs.get('pk2'))
#         except Client.DoesNotExist:
#             raise Http404
#         try:
#             subscription = client.subscription_set.get(id=self.kwargs.get('pk3'))
#             return subscription
#         except Subscription.DoesNotExist:
#             raise Http404
#     serializer_class = SubscriptionSerializer
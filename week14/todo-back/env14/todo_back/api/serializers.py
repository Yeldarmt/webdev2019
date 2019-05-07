from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Task, TaskList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    def create(self, validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(read_only=True)
    task_list_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'created_by', 'task_list_id')

class TaskSerializer3(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'created_by', 'task_list_id')




class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    tasks = TaskSerializer3(many=True)
    #tasks = serializers.StringRelatedField(many=True)
    #tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        tasklist = TaskList.objects.create(**validated_data)
        for task in tasks:
            Task.objects.create(task_list=tasklist, **task)
        # arr = [Task(task_list=tasklist, **task) for task in tasks]
        # Task.objects.bulk_create(arr)
        # for i in range(0, len(arr), 100):
        #     Task.objects.bulk_create(arr[i:i+100])
        return tasklist

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    status = serializers.CharField()


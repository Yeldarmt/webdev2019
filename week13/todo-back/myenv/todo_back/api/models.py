from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user).order_by('name')

class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    objects = TaskListManager()
    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return '{} : {} '.format(self.id, self.name)

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }



# from django.db import models
#
# # Create your models here.
#
#
# class Gym(models.Model):
#     name = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     def str(self):
#         return self.name
#
#
# class Coach(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     photo = models.ImageField()
#     experience = models.IntegerField()
#     work_days = models.CharField(max_length=200)
#     gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, null=True)
#
#     def str(self):
#         return self.name
#
#
# class Client(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     age = models.IntegerField()
#     status = models.CharField(max_length=200)
#     registered_date = models.DateTimeField()
#     coach = models.ForeignKey(Coach, on_delete=models.CASCADE, default=None, null=True)
#     gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, null=True)
#
#     def str(self):
#         return self.name
#
#
# class Test(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None, null=True)
#     height = models.IntegerField()
#     weight = models.FloatField()
#     chest_girth = models.FloatField()
#     waist_circumference = models.FloatField()
#     hip_girth = models.FloatField()
#     body_type = models.CharField(max_length=200)
#
#     def str(self):
#         return self.client.name
#
#
# class Subscription(models.Model):
#     card_number = models.CharField(max_length=200)
#     price = models.IntegerField()
#     duration = models.CharField(max_length=200)
#     has_coach = models.BooleanField(default=False)
#     allowed_from = models.TimeField()
#     allowed_until = models.TimeField()
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None, null=True)
#
#     def str(self):
#         return self.client.name
#
#
# class Feedback(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None, null=True)
#     date = models.DateTimeField()
#     comment = models.CharField(max_length=1000)
#     gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, null=True)
#
#     def str(self):
#         return self.client.name
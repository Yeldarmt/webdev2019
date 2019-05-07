from django.urls import path
from api import views

#fbv
# urlpatterns = [
#     path('task_lists/', views.task_lists),
#     path('task_lists/<int:num>/', views.task_list_num),
#     path('task_lists/<int:num>/tasks/', views.task)
# ]

#cbv
# urlpatterns = [
#     path('task_lists/', views.Tasklist.as_view()),
#     path('task_lists/<int:num>/', views.TaskList_detail.as_view()),
#     path('task_lists/<int:num>/tasks/', views.Task.as_view())
# ]


# urlpatterns = [
#     path('task_lists/', views.task_lists),
#     path('task_lists/<int:num>/', views.TaskList_detail.as_view()),
#     path('task_lists/<int:num>/tasks/', views.Task.as_view())
# ]

#generics
urlpatterns = [
    path('task_lists/', views.TaskListt.as_view()),
    path('task_lists/<int:pk>/', views.TaskList_detail.as_view()),
    #path('task_lists/<int:pk>/tasks/', views.Task.as_view()),
    path('task_lists/<int:pk>/tasks/', views.TaskListTasks.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)
]
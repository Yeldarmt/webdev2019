from django.urls import path, re_path
from api import views
urlpatterns = [
    # path('', views.index),
    # path('about/', views.about),
    # path('about/plus/<int:pk>/', views.about_repath),
    path('task_lists/', views.task_list),
    path('task_lists/<int:num>/', views.task_list_num),
    path('task_lists/<int:num>/tasks/', views.task_list_tasks)
]
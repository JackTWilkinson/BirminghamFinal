from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('resume/view', views.work_experience_list, name='work_experience_list'),
    path('work_experience/new', views.work_experience_new, name='work_experience_new'),
    path('work_experience/<int:pk>/edit', views.work_experience_edit, name='work_experience_edit'),
    path('work_experience/<int:pk>/', views.work_experience_detail, name='work_experience_detail'),
]
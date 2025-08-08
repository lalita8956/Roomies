from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorkListView.as_view(), name='work_list'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('days/', views.DayListView.as_view(), name='day_list'),
]
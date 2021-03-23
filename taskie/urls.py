from django.urls import path
from . import views

urlpatterns = [
    path ('', views.defacto, name = "tasks"),
    path('update<str:pkey>', views.updateTask, name = "update"),
    path('delete<str:pkey>', views.deleteTask, name = "del"),
]
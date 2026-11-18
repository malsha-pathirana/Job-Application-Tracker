from django.urls import path
from . import views

urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add/',views.add_job,name='add_job'),
    path('edit/<int:pk>',views.edit_job,name='edit_job'),
    path('delete/<int:pk>',views.delete_job,name='delete_job'),
]
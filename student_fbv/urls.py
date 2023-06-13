from django.urls import path
from . import views

app_name = 'studentFbv'

urlpatterns = [
    path('', views.student_list),
    path('detail/<int:pk>/', views.student_detail),
]

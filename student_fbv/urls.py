from django.urls import path
from . import views

app_name = 'studentFbv'

urlpatterns = [
    path('', views.student_list),
    path('<int:pk>/', views.student_detail),
]

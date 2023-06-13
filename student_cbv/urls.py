from django.urls import path
from . import views

app_name = 'studentCbv'

urlpatterns = [
    path('', views.StudentList.as_view()),
    path('<int:pk>/', views.StudentDetail.as_view()),
]

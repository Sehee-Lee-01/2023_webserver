from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'studentCbv'

urlpatterns = [
    path('', views.StudentList.as_view()),
    path('<int:pk>/', views.StudentDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

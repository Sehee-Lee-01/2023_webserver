from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'studentFbv'

urlpatterns = [
    path('', views.student_list),
    path('<int:pk>/', views.student_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)

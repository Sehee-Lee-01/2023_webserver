from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'post'
router = DefaultRouter()
router.register('', views.PostViewSet)
urlpatterns = [
    path('public/', views.public_post_list),
    path('', include(router.urls)),
]

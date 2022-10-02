from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = []+router.urls

# 127.0.0.1.8000/posts

# basename used to identify a particular post

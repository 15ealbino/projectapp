from django.urls import path, include
from .api import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet,basename='user')
router.register('project',ProjectViewSet,basename='project')
router.register('tag',TagViewSet,basename='tag')
router.register('projectbacklog',ProjectBackLogViewSet,basename='projectbacklog')
router.register('projectmessagebox', ProjectMessageBoxViewSet,basename='projectmessagebox')
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('clients', views.ClientViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
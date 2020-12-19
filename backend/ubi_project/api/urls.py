from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('clients', views.ClientViewSet)
router.register('contents', views.ContentViewSet)
router.register('contenthighlights', views.ContentHighlightViewSet)
router.register('contentsiblings', views.ContentSiblingViewSet)
router.register('contentupselling', views.ContentUpsellingViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]

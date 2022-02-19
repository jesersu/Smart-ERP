from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'dos/', views.ArticleViewSet)

urlpatterns = router.urls

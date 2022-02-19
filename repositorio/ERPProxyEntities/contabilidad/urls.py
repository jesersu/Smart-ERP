""" from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('', views.ArticleViewSet)
router.register('dos', views.getTiposDocumento)
urlpatterns = [
    path('', include(router.urls)),
]
 """

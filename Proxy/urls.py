from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .routers import router
from repositorio.ERPProxyEntities.contabilidad import views

# Wire up our API using automatic URL routing.
# Additionally, login URLs included for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path("api/v1/tipoDocumento", views.gettipodocumento),

    path("MSFacturacionQry/",
         include('controllers.FacturacionController.urls')),

    path("MSLogisticaQry/",
         include('controllers.LogisticaController.urls')),

    path("MSPlanillas/",
         include('controllers.LogisticaController.urls')),

    #path("api/v1/param", views.parametrosget),
    #path("api/v1/entidades/", views.TipoViewSet.as_view()),



]

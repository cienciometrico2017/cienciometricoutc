from django.conf.urls import url
from apps.principal.views import inde,producc,similar,grafica
from django.contrib.auth.decorators import login_required
from .views import BusquedaView, BusquedaAjaxView,BusquedaFacuView, BusquedaCampusView,BusquedaCarreraView
urlpatterns = [
    url(r'^$',inde, name="principal"),
    url(r'^base/cientifica$',producc, name="produccion"),
    url(r'^base/similares$',similar, name="similar"),
    url(r'^base/graficas$', BusquedaView.as_view(), name="grafic"),
    url(r'^base/busqueda_ajax/$',BusquedaAjaxView.as_view()),
    url(r'^base/busqueda_campus/$',BusquedaCampusView.as_view()),
    url(r'^base/busqueda_facultad/$',BusquedaFacuView.as_view()),
        url(r'^base/busqueda_carrera/$',BusquedaCarreraView.as_view()),



]

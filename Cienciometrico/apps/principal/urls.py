from django.conf.urls import url
from apps.principal.views import inde,producc,similar,grafica
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',inde, name="principal"),
    url(r'^cientifica$',producc, name="produccion"),
    url(r'^similares$',similar, name="similar"),
    url(r'^graficas$', grafica, name="grafic"),

]
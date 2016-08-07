from django.conf.urls import url
from receitas import views

urlpatterns = [
    url(r'^receitas/$', views.receitas_list),
    url(r'^receitas/(?P<pk>[0-9]+)/$', views.receita_detalhe),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^AreaLogada$', views.area_logada, name='area_logada'),
    url(r'^sobre$', views.sobre, name='sobre'),
    url(r'^login$', views.entrar, name='login'),
    url(r'^logout$', views.sair, name='logout'),
    url(r'^cadastro_sucesso$', views.cadastro_sucesso, name='cadastro_sucesso')
]
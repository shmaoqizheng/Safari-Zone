from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^safari/(?P<zone>\w+)$', views.area),
    url(r'^findPokemon/(?P<action>\w+)$', views.pokemon),
    url(r'^battle$', views.battlePokemon)
]

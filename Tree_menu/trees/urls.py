from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index),
    url("^(?P<id>\d+)/", views.index, name="menu"),
]

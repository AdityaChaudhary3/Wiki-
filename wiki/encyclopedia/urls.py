from random import random
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.show, name="show"),
    path("create/", views.create, name="create"),
    path("search/", views.search, name="search"),
    path("random/", views.randm, name="random"),
    path("edit/", views.edit, name="edit"),
    path("save_edit/", views.save_edit, name="save_edit")
]

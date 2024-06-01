from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.ShowAll.as_view(), name="all_cloth"),
    path("old_cloth/", views.ShowOld.as_view(), name="old_cloth"),
    path("young_cloth/", views.ShowKids.as_view(), name="young_cloth"),
]

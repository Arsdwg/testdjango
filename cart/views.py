from django.shortcuts import render
from django.views import generic
from . import models


class ShowAll(generic.ListView):
    template_name = "cart/product_list.html"
    context_object_name = "clothes"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class ShowOld(generic.ListView):
    template_name = "cart/old_cloth.html"
    context_object_name = "old"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="old").order_by("-id")


class ShowKids(generic.ListView):
    template_name = "cart/kid_cloth.html"
    context_object_name = "kids"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="kids").order_by("-id")

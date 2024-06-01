# Create your views here.
from django.shortcuts import get_object_or_404
from django.views import generic
from . import models, forms


# Create your views here.


# List
class PostNotFull(generic.ListView):
    template_name = "post.html"
    context_object_name = "posts"
    model = models.PostItem

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class CreateReviewItem(generic.CreateView):
    template_name = "create_review.html"
    form_class = forms.ReviewForm
    success_url = "/items/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewItem, self).form_valid(form=form)


# Detail
class PostMore(generic.DetailView):
    template_name = "post_detail.html"
    context_object_name = "post_id"

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(models.PostItem, id=post_id)


from django.urls import path
from . import views

urlpatterns = [
    # path("books/", views.PostNotFull.as_view(), name="books"),
    # path("books/<int:id>/", views.PostMore.as_view(), name="detail"),
    # path("books/<int:id>/delete/", views.DeleteBook.as_view(), name="delete"),
    # path("books/<int:id>/update/", views.UpdateBook.as_view(), name="update"),
    # path("create/", views.CreateBook.as_view(), name="create"),
    # path("create_review/", views.CreateReviewBook.as_view(), name="create_review"),
    path('items/', views.PostNotFull.as_view(), name='list'),
    path("items/<int:id>/", views.PostMore.as_view(), name="detail"),
    path("create_review/", views.CreateReviewItem.as_view(), name="create_review")

]

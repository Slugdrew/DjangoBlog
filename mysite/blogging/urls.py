from django.urls import path
from django.conf.urls import url
# from blogging.views import stub_view
from blogging.views import BloggingListView, BloggingDetailView

urlpatterns = [
    path('', BloggingListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', BloggingDetailView.as_view(), name="blog_detail"),
]
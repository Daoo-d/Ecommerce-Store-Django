from django.urls import path
from . import views

urlpatterns = [
    path("",views.PostList.as_view(),name="posts-page"),
    path("posts/<slug>", views.IndividualPost.as_view(),name="post-details"),
    path("search/",views.search_blog,name = "search_blog")
]

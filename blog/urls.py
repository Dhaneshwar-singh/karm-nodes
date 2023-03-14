from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"  ),
    path("page/<slug:slug>/", views.page_detail, name="page_detail"  ),
]

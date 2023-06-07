from django.urls import path

from .views import FrontPage, PostByTag, PostDetail, PostList

urlpatterns = [
    path('', FrontPage.as_view(), name='frontpage'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag')
]
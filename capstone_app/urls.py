
from django.urls import path
from.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    LikesView
)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('about/',views.about,name='info'),
    path('search/',views.search,name='search'),
    path('likes/<int:pk>',LikesView,name='like_movies'),
    ]
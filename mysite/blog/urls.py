from django.conf.urls import url,include
from . import views


urlpatterns = [
    url('',views.PostListView.as_view(),name='post_list'),
    url('about/',views.AboutView.as_view(),name='about'),
    url('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    url('post/new/', views.CreatePostView.as_view(), name='post_new'),
    url('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),

    ]

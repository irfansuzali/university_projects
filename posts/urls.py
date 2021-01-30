from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name = 'post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post_delete'),
    path('new/', views.PostCreateView.as_view(), name = 'post_new'),
    path('comment_new/', views.CommentCreateView.as_view(), name = 'comment_new'),
    path('category/<str:category>/', views.CategoryListView, name = 'category_list'),
    path('school/<str:school>/', views.SchoolListView, name = 'school_list')
]
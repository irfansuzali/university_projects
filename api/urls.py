from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

#Replaced urls with router to use with viewsets
router = SimpleRouter()
router.register('users', views.UserViewSet, basename = 'Users')
router.register('posts', views.PostViewSet, basename = 'Posts')
router.register('categories', views.CategoryViewSet, basename = 'Categories')
router.register('comments', views.CommentViewSet, basename = 'Comments')
router.register('schools', views.SchoolViewSet, basename = 'Schools')

urlpatterns = router.urls
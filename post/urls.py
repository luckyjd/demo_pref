from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(f'user', views.UserViewSet, basename="user")
router.register(f'post', views.PostViewSet, basename="post")
router.register(f'comment', views.CommentViewSet, basename="comment")


urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="postlist"),
    path("post/<int:post_id>/", views.detail, name="detail")
]
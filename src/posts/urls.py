from django.urls import path

from .views import list_post,post_detail,post_create
urlpatterns = [
    path('',list_post),
    path('<int:post_id>/',post_detail),
    path('create/',post_create),
]

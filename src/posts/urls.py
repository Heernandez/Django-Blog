from django.urls import path

from .views import (list_post,post_detail,post_create,post_update)
urlpatterns = [
    path('',list_post,name = "posts"),
    path('<int:post_id>/update/',post_update),
    path('<int:post_id>/',post_detail,name = "posts"),
    
    path('create/',post_create,name = "new"),
    
]

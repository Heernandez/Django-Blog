from django.urls import path

from .views import list_post
urlpatterns = [
    path('',list_post)
]

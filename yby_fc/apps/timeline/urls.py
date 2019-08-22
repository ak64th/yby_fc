from django.urls import path

from . import views

app_name = 'timeline'
urlpatterns = [
    path(
        'post/',
        views.PostViewSet.as_view({'get': 'list'}),
        name='post_list',
    ),
    path(
        'post/<int:pk>/',
        views.PostViewSet.as_view({'get': 'retrieve'}),
        name='post_details',
    ),
]

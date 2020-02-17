from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('detail/<int:post_id>/' , views.post_detail , name = 'detail'),
    path('new_post/',views.PostCreateView.as_view(),name='new_post'),
    path('detail/<slug:pk>/update/',views.PostUpdateView.as_view(),name='post_update'),
    path('detail/<slug:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),
]
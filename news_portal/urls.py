from django.urls import path
from .views import PostList, PostDetail, post_create, PostUpdate, PostDelete

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('news/create/', post_create),
   path('articles/create/', post_create),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
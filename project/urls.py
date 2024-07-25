from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('posts/', include('news_portal.urls')),
   path('posts/search', include('news_portal.urls')),
   path('', include('news_portal.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
]


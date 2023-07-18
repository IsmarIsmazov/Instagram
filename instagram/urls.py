from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from instagram import settings
from .yasg import urlpatterns as doc_urls




urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('media_part.urls')),
] + static(settings.STATIC_URL, document_url=settings.STATIC_URL)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

urlpatterns += doc_urls







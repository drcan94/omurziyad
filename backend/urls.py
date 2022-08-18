from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('api/user/', include('base.urls.user_urls')),
    path('api/omur/', include('base.urls.omur_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

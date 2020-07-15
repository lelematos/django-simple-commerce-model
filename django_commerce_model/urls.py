from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('posts.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                       document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                    document_root=settings.MEDIA_ROOT)

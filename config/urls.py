from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('', include('main.urls')),
    # path('search/', include('search.urls')),
    # path('', include('account.urls')),
]

urlpatterns += i18n_patterns(
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('main.urls')),
    path('search/', include('search.urls')),
    path('', include('account.urls')),
)

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path , include
from user import urls as user_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LUXOROSH_Homepage.urls')),
    path('', include(user_urls)),

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

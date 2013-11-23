from django.conf.urls import patterns, include, url
from app.views import SoundView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', SoundView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

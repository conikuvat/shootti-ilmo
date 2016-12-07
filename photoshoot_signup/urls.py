from django.conf.urls import include, url

from django.contrib import admin

from .views import index_view, protected_view


admin.autodiscover()

urlpatterns = [
    url(r'', include('kompassi_oauth2.urls')),
    url(r'^$', index_view, name='index_view'),
    url(r'^protected/?$', protected_view, name='protected_view'),
    url(r'^admin/', include(admin.site.urls)),
]

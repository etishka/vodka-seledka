from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vodka_seledka_com.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

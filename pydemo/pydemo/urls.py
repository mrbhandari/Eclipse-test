from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import my_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pydemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', my_view),
)

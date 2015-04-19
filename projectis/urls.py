from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myprojectapp.views.base', name='home'),
    url(r'^dashboard/$', 'myprojectapp.views.dashboard', name='dashboard'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    
)

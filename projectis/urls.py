from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myprojectapp.views.base', name='home'),
    url(r'^add_classes/$', 'myprojectapp.views.add_classes', name='add_classes'),
    url(r'^update_class/$', 'myprojectapp.views.update_class', name='update_class'),

    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myprojectapp.views.base', name='home'),
    url(r'^add_classes/$', 'myprojectapp.views.add_classes', name='add_classes'),
    url(r'^delete_class/$', 'myprojectapp.views.delete_class', name='delete_class'),

    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

)

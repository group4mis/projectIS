from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myprojectapp.views.base', name='home'),
    url(r'^add_classes/$', 'myprojectapp.views.add_classes', name='add_classes'),
    url(r'^delete_classes/$', 'myprojectapp.views.delete_classes', name='delete_classes'),
    url(r'^grades$','myprojectapp.views.grades',name='grades'),
    url(r'Show_Tmeetings$','myprojectapp.views.Show_Tmeetings',name='Requested meetings')
    url(r'Show_Pmeetings$','myprojectapp.views.Show_Pmeetings',name='Requested meetings')
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)

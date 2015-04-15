from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'projectis.views.base', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^$', 'projectis.views.registration', name='registration'),
)

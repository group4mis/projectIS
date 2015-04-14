from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'projectis.views.base', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html'))
)
 #bl video 7a6 ena nbdl elklma w n76 bdalha joins.view  b a5r s6r code hni bs hni mafe .view.home :/

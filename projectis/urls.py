from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'myprojectapp.views.t_classes', name='home'),
    url(r'^t_classes/$','myprojectapp.views.t_classes',name='t_classes'),
    url(r'^p_classes/$','myprojectapp.views.p_classes',name='p_classes'),
    url(r'^s_classes/$','myprojectapp.views.s_classes',name='s_classes'),
    #url(r'^add_classes/$', 'myprojectapp.views.add_classes', name='add_classes'),
    #url(r'^delete_classes/$', 'myprojectapp.views.delete_classes', name='delete_classes'),
    url(r'^Show_Tmeetings/$','myprojectapp.views.Show_Tmeetings',name='Show_Tmeetings'),
    url(r'^Show_Pmeetings/$','myprojectapp.views.Show_Pmeetings',name='Show_Pmeetings'),
    url(r'^Show_Snotes/$','myprojectapp.views.Show_Snotes',name='Show_Snotes'),
    url(r'^Show_Bnotes/$','myprojectapp.views.Show_Bnotes',name='Show_Bnotes'),
    url(r'^s_show_grade/$','myprojectapp.views.s_show_grade',name='s_show_grade'),
    url(r'^p_show_grade/$','myprojectapp.views.p_show_grade',name='p_show_grade'),
    url(r'^class_details/(?P<class_id>\d+)/$','myprojectapp.views.class_details',name='class_details'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^s_show_attendance/$','myprojectapp.views.s_show_attendance',name='s_show_attendance'),
    url(r'^p_show_attendance/$','myprojectapp.views.p_show_attendance',name='p_show_attendance'),


)

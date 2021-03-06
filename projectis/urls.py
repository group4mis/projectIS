from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'myprojectapp.views.all_classes', name='home'),
    url(r'^t_classes/$','myprojectapp.views.t_classes',name='t_classes'),
    url(r'^p_classes/$','myprojectapp.views.p_classes',name='p_classes'),
    url(r'^s_classes/$','myprojectapp.views.s_classes',name='s_classes'),
    url(r'^$', 'myprojectapp.views.show_meeting', name='show_meeting'),
    url(r'^t_show_meetings/$','myprojectapp.views.t_show_meetings',name='t_show_meetings'),
    url(r'^p_show_meetings/$','myprojectapp.views.p_show_meetings',name='p_show_meetings'),
    url(r'^$', 'myprojectapp.views.show_snotes', name='show_snotes'),
    url(r'^s_show_snotes/$','myprojectapp.views.s_show_snotes',name='s_show_snotes'),
    url(r'^p_show_snotes/$','myprojectapp.views.p_show_snotes',name='p_show_snotes'),
    url(r'^show_bnotes/$','myprojectapp.views.show_bnotes',name='show_bnotes'),
    url(r'^$', 'myprojectapp.views.show_grade', name='show_grade'),
    url(r'^s_show_grade/$','myprojectapp.views.s_show_grade',name='s_show_grade'),
    url(r'^p_show_grade/$','myprojectapp.views.p_show_grade',name='p_show_grade'),
    url(r'^t_show_grade/$','myprojectapp.views.t_show_grade',name='t_show_grade'),
    url(r'^$', 'myprojectapp.views.show_attendance', name='show_attendance'),
    url(r'^s_show_attendance/$','myprojectapp.views.s_show_attendance',name='s_show_attendance'),
    url(r'^p_show_attendance/$','myprojectapp.views.p_show_attendance',name='p_show_attendance'),
    url(r'^t_show_attendance/$','myprojectapp.views.t_show_attendance',name='t_show_attendance'),
    url(r'^$', 'myprojectapp.views.all_classes_details', name='all_classes_details'),
    url(r'^t_class_details/(?P<class_id>\d+)/$','myprojectapp.views.t_class_details',name='t_class_details'),
    url(r'^p_class_details/(?P<class_id>\d+)/$','myprojectapp.views.p_class_details',name='p_class_details'),
    url(r'^s_class_details/(?P<class_id>\d+)/$','myprojectapp.views.s_class_details',name='s_class_details'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^p_request_meeting/$','myprojectapp.views.p_request_meeting',name='p_request_meeting'),
    url(r'^p_r_m/$','myprojectapp.views.p_r_m',name='p_r_m'),
    
)

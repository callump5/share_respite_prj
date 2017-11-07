from django.conf.urls import url
import views

urlpatterns = [
    url(r'forum/$', views.forum, name='forum'),
    url(r'forum/subject/(?P<subject_id>\d+)/$', views.subject_details, name='subject'),
    url(r'^subject/(?P<subject_id>\d+)/new/thread$', views.new_thread, name='new_thread'),
    url(r'^subject/(?P<subject_id>\d+)/edit/thread/(?P<thread_id>\d+)/$', views.edit_thread, name='edit_thread'),
    url(r'^subject/(?P<subject_id>\d+)/delete/thread/(?P<thread_id>\d+)/$', views.delete_thread, name='delete_thread'),
    url(r'^subject/(?P<subject_id>\d+)/view/thread/(?P<thread_id>\d+)/$', views.view_thread, name='view_thread'),
    url(r'^subject/(?P<subject_id>\d+)/thread/(?P<thread_id>\d+)/new/comment/$', views.new_comment, name='new_comment')
]
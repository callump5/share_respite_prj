from django.conf.urls import url

from django.contrib.auth import views as auth_views
import views
urlpatterns = [
    url(r'^register/$', views.signup, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    ]
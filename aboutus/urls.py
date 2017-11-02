from django.conf.urls import url
import views

urlpatterns = [
    url(r'^about-us/staff/$', views.staff_list, name='staff'),
    url(r'^about-us/whats-on/$', views.whats_on, name='whats_on'),
]

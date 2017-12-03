from django.conf.urls import url
import views

urlpatterns = [
    url(r'^donate/$', views.donate, name='donation'),
    url(r'^donations/$', views.donations),
    url(r'^donation-data/$', views.get_donations, name='donations'),

]

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^donate/$', views.donate, name='donation'),
    url(r'^donations/$', views.donation_graphs),
    url(r'^donation-data/$', views.donation_data),

]

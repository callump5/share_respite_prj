from django.conf.urls import url
import views

urlpatterns = [
    url(r'^donate/$', views.donate, name='donation'),

]

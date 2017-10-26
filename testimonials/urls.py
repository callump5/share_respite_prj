from django.conf.urls import url
import views

urlpatterns = [
    url(r'^testimonials/$', views.testimonial_list, name='testimonials'),
    url(r'^testimonials/new/$', views.new_testimonial, name='new_testimonial')
]

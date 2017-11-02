from django.conf.urls import url
import views

urlpatterns = [
    url(r'^testimonials/$', views.testimonial_list, name='testimonials'),
    url(r'^testimonials/new/$', views.new_testimonial, name='new_testimonial'),
    url(r'^testimonials/delete/(?P<post_id>\d+)/$', views.delete_testimonial, name='delete_testimonial'),
    url(r'^testimonials/edit/(?P<post_id>\d+)/$', views.edit_testimonial, name='edit_testimonial'),
]

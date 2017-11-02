"""share_respite_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT

from home import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Images
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # Home Page
    url(r'^$', home_views.get_index, name='home'),

    # Accounts
    url(r'^', include('accounts.urls')),

    # Testimonials
    url(r'^', include('testimonials.urls')),

    # About Us
    url(r'^', include('aboutus.urls'))


]

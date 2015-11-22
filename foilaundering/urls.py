# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic import TemplateView



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home_page.html")),
    url(r'^request/', include('foi_requests.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

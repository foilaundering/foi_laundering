from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'submit/$', views.SubmitView.as_view(), name="submit"),
    url(r'thanks/$', TemplateView.as_view(template_name="submit_thanks.html")),
    url(r'list_requests/$', views.RequestsListView.as_view(), name="list_requests"),
]

from django.conf.urls import url
from django.views.generic import ListView
from web_app.models import Object
from . import views

urlpatterns = [
    # url(r'^$', views.web_app, name='web'),
    # url(r'^$', views.ObjectView.as_view(), name='object'),
    url(r'^$', ListView.as_view(queryset=Object.objects.all(), template_name='web_app/web.html')),
]

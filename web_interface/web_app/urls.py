from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^$', views.web_app, name='web'),
    url(r'^$', views.ObjectView.as_view(), name='object'),
]

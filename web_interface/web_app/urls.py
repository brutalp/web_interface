from django.conf.urls import url
from django.views.generic import ListView
from web_app.models import Value
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    # url(r'^$', views.web_app, name='web'),
    # url(r'^$', views.ObjectView.as_view(), name='object'),
    # url(r'^$', ListView.as_view(queryset=Value.objects.all()[:50], template_name='web_app/web.html')),
    # url('web_test/', views.PagViewTest, name='pagination'),
    path('web/', PagView.as_view(), name='pagination'),
    path('web/<int:page_id>', PagView.as_view()),
]

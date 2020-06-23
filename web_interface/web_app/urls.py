from django.urls import path
from .views import *

urlpatterns = [
    path('web/', IndexView.as_view(), name='index'),
]
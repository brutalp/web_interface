from django.shortcuts import render
from django.views import generic
from web_app.models import Object


def web_app(request):
    return render(request, 'web_app/web.html')


class ObjectView(generic.ListView):
    model = Object

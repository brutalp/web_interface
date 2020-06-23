from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import *
import json


class IndexView(View):
    def get(self, request, page_id=1):

        if not request.is_ajax():
            value_list = Measurmement.objects.all().order_by('id')
            page = request.GET.get('page', 1)
            paginator = Paginator(value_list, 50)
            try:
                values = paginator.page(page_id)
                values.num_pages_tuple = tuple(range(paginator.num_pages))
            except:
                return redirect(reverse('pagination'))
            return render(request, 'web_app/index.html', {'values': values})
        else:
            values_list = [value for value in Measurmement.objects.values()]
            values_list = json.dumps({'values': values_list}, indent=4, sort_keys=True, default=str)
            print('#################AJAX###############')
            # print(values_list)
            return HttpResponse(values_list, content_type='application/json')
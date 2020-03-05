from django.shortcuts import render

def web_app(request):
    return render(request, 'web_app/web.html')

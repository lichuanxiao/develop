from django.shortcuts import render

# Create your views here.


def releasenote(request):
    return render(request, 'index/index.html')

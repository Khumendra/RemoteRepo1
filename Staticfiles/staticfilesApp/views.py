from django.shortcuts import render


def index(request):
    heading = {'heading': 'This is from Static Files'}
    return render(request, 'staticfilesApp/index.html', context=heading)

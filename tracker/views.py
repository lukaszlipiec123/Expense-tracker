from django.shortcuts import render


def home(request):
    return render(request, 'tracker/home.html')


def page(request):
    return render(request, 'tracker/page.html')

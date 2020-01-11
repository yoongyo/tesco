from django.shortcuts import render


def ceo(request):
    return render(request, 'introduction/ceo.html')


def history(request):
    return render(request, 'introduction/history.html')


def overview(request):
    return render(request, 'introduction/overview.html')

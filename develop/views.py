from django.shortcuts import render


def develop(request):
    return render(request, 'develop/develop.html')

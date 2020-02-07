from django.shortcuts import render
import sys
sys.path.append('..')
from introduction.models import Customer


def home(request):
    customers = Customer.objects.all()
    return render(request, 'home.html', {
        'customers': customers
    })


def robots(request):
    return render(request, 'robots.txt')


def owner(request):
    return render(request, 'naverfd014607792a788dc788160885065616.html')

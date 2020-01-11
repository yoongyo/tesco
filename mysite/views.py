from django.shortcuts import render
import sys
sys.path.append('..')
from introduction.models import Customer


def home(request):
    customers = Customer.objects.all()
    return render(request, 'home.html', {
        'customers': customers
    })

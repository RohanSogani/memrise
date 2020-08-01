from django.shortcuts import render
from django.http import HttpResponse

cards = [
    {
        'word': 'Nice',
        'mnemonic': 'Something good',
        'date_created': 'July 30, 2020'
    }, 
    {
        'word': 'Pretty',
        'mnemonic': 'Something nice',
        'date_created': 'July 31, 2020'
    }
]

def home(request):
    context = {
        'cards': cards
    }
    return render(request, 'cards/home.html', context)

def about(request):
    return render(request, 'cards/about.html')

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

posts = [
    {
        'author': 'holey',
        'title': 'shit',
        'description': 'is',
        'text': 'that shit!?'
    },
    {
        'author': 'that',
        'title': 'is',
        'description': 'unbelievable',
        'text': 'shit!'
    }
]


@csrf_exempt 
def index(request):
    if request.method == 'POST':
        return JsonResponse({'profile': posts})
    return HttpResponse("Hello, world. You're at the /api index page.")

def profile(request):
    return JsonResponse({'profile': posts})

def products(request):
    return JsonResponse({'profile': posts})

def categories(request):
    return JsonResponse({'profile': posts})

def category(request, category_id):
    return HttpResponse("You're voting on category %s." % category_id)

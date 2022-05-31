from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Product.models import Product, Category

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

def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse({
            'products': list(products.values())
        })

@csrf_exempt 
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return JsonResponse({
            'categories': list(categories.values())
        })
    if request.method == 'POST':
        name = request.GET.get("category_name", None)
        if not name:
            return JsonResponse({"status": False, "msg": "Bad name param"})
        
        new_category = Category()
        new_category.category_text = name

        existed_category = Category.objects.filter(category_text=name)

        if len(existed_category) > 0:
            return JsonResponse({"status": False, "msg": "Item with that name already exist"})
        else:
            new_category.save()
            return JsonResponse({
                "status": True, 
                "msg": "Item was added",
                'Id': new_category.id
            })


@csrf_exempt 
def find_categories(request):
    if request.method == 'POST':
        name = request.GET.get("category_name", None)
        queryset = Category.objects.filter(category_text__icontains=name).values()
        return JsonResponse({
            'category': list(queryset)
        })


@csrf_exempt 
def category(request, category_id):
    if request.method == 'GET':
        queryset = Category.objects.filter(id=category_id).values()
        return JsonResponse({
            'category': list(queryset)
        })

    elif request.method == 'POST':
        name = request.GET.get("category_name", None)
        if not name:
            return JsonResponse({"status": False, "msg": "Bad name param"})

        categories = Category.objects.filter(id=category_id)

        if len(categories) <= 0:
            return JsonResponse({"status": False, "msg": "Item with that id not exist"})
            
        for cat in categories:
            cat.category_text = name
            cat.save()
        
        return JsonResponse({"status": True, "msg": "Item was updated"})

    elif request.method == 'DELETE':
        categories = Category.objects.filter(id=category_id)

        if len(categories) <= 0:
            return JsonResponse({"status": False, "msg": "Item with that id not exist"})

        for cat in categories:
            cat.delete()

        return JsonResponse({"status": True, "msg": "Item was deleted"})
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('categories', views.categories, name='categories'),
    path('find_categories', views.find_categories, name='find_categories'),
    path('category/<int:category_id>/', views.category, name='category'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('products', views.products, name='products'),
    path('categories', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category, name='category'),
]
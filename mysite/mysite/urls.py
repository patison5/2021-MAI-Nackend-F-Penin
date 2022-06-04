from django.contrib import admin
from django.urls import path

from Upload.views import image_upload
from Product.views import ProductAPIView, CategoryAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/productlist/', ProductAPIView.as_view()),
    path('api/v1/categorylist/', CategoryAPIView.as_view()),
    path("", image_upload, name="upload"),
]

from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
import api.views as view_api

router = DefaultRouter()

router.register('customer',view_api.CustomerViewSet,basename = 'customer')
router.register('product',view_api.ProductViewSet,basename = 'product')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

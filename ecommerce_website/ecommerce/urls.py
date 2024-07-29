from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    product_list,
    product_detail,
    add_to_cart,
    view_cart,
    checkout,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path("<int:product_id>/", product_detail, name="product_detail"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name="checkout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

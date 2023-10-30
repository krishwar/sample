from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.home),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
path('cart/', views.cart, name='cart'),
path('payment/', views.payment_details, name='payment_details'),
path('checkout/', views.checkout, name='checkout'),
    path("category/<slug:val>", views.categoryView.as_view(),name="category"),
    path('register/', views.register_view, name='register'), path('login/', views.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

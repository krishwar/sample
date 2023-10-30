from django.shortcuts import render
from django.db.models import Count
from urllib import request
from django.views import View
from . models import Product
from django.contrib.auth import login, authenticate
def login_signup_view(request):
return render(request, 'your_app/login_signup.html')

# Create your views here.
def home(request):
    return render(request,"app/home.html")
def payment_details(request):
if request.method == 'POST': # Process the form data
name = request.POST.get('name')
card_number = request.POST.get('card_number') expiry = request.POST.get('expiry')
cvv = request.POST.get('cvv')
 
return render(request, 'payment_details.html')

def checkout(request):
if request.method == 'POST':
    return redirect('order_confirmation') # Replace with your confirmation page URL products = Product.objects.all()
    context = {
        'products': products,
}
return render(request, 'checkout.html', context)

class categoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,"app/category.html",locals())
def add_to_cart(request, product_id):
cart, created = Cart.objects.get_or_create(user=request.user) product = get_object_or_404(Product, pk=product_id)
cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product) if not item_created:
cart_item.quantity += 1 cart_item.save()
cart.total += product.price cart.save()
return redirect('cart')
def remove_from_cart(request, cart_item_id):
cart_item = get_object_or_404(CartItem, pk=cart_item_id) cart_item.cart.total -= cart_item.price
cart_item.cart.save() cart_item.delete() return redirect('cart')
def cart(request):
cart, created = Cart.objects.get_or_create(user=request.user) cart_items = CartItem.objects.filter(cart=cart)
context = {'cart_items': cart_items} return render(request, 'cart.html', context)

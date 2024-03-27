from django.shortcuts import render, get_object_or_404
from .cart import Cart
from home.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    #get the cart
    cart=Cart(request)
    cart_products=cart.get_prods
    return render(request, "cart_summary.html", {"cart_products":cart_products})

def cart_add(request):
    #Get the cart
    cart=Cart(request)

    #testing for POST
    if request.POST.get('action') == 'post':
        #get the items/stuff
        product_id=int(request.POST.get('product_id'))

        #looking up for product in our database
        product=get_object_or_404(Product, id=product_id)

        #Now this is saving it to a session so that the product new leaves the the cart event if we exit the site
        cart.add(product=product)


        #Get Cart Quantity
        cart_quantity=cart.__len__()

        #Return response
        #response=JsonResponse({'Product Name:': product.name})
        response=JsonResponse({'qty:': cart_quantity})
        return response
    

def cart_delete(request):
    pass

def cart_update(request):
    pass
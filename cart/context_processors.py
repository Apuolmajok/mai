from .cart import Cart

#CREATING CONTEXT PROCESSOR SO OUR CART CAN WORK ON ALL PAGES OF QUICK NOVA
def cart(request):
    #return the default data from our cart
    return{'cart':Cart(request)}
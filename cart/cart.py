from home.models import Product

class Cart():

    def __init__(self, request):
        self.session=request.session

        #GET CURRENT SESSION KEY IF IT EXISTS
        cart=self.session.get('session_key')

        #if the user is new, then no session key for them, ccreate one
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        #Make sure cart is avaialble on all pages of our quick nova site
        self.cart=cart

    def add(self, product):
        product_id=str(product.id)

        #logic of whether it has been added or not
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]={'price': str(product.price)}


        self.session.modified=True


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #Get ids from cart
        product_ids=self.cart.keys()

        #use ids to look for products in database models
        products=Product.objects.filter(id__in=product_ids)

        #Return thoselooked up products
        return products
        

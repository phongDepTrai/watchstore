from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()
    if request.method == 'POST':
        print("I'm here")
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order = order,product = item['product'],price = item['fee'], quantity = item['quantity'])
                #clear the cart
                cart.clear()
                return render(request, 'orders/created.html', context = {'order' :order}) 
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html',context={'form':form})
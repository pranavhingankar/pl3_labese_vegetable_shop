from django.shortcuts import render, redirect
from django.views import View
from .models import Customer , Product , Cart , OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse



class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html',{'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles,'laptops':laptops})





def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Cart(user=user, product=product).save()

    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        #print(cart)
        amount = 0.0
        shipping_amount= 70.0
        totalamount = 0.0
        tempamount = 0.00
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        #print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = ((p.quantity) * (p.product.discounted_price))
                amount = amount + tempamount
                totalamount = amount + shipping_amount

            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
 
        else:
            return render(request, 'app/emptycart.html')

def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        amount = 0.00
        shipping_amount = 70.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = ((p.quantity) * (p.product.discounted_price))
            amount = amount + tempamount
            

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -=1
        c.save()
        amount = 0.00
        shipping_amount = 70.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = ((p.quantity) * (p.product.discounted_price))
            amount = amount + tempamount
            

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        
        c.delete()
        amount = 0.00
        shipping_amount = 70.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = ((p.quantity) * (p.product.discounted_price))
            amount = amount + tempamount
               

        data = {
            'amount':amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


        


# def profile(request):
#  return render(request, 'app/profile.html')


def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})

# def change_password(request):
#  return render(request, 'app/changepassword.html')
 


def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
        {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have successfully Registered')
            form.save()
        return render(request, 'app/customerregistration.html',
        {'form': form})








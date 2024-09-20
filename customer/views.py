from django.shortcuts import render,redirect
from  . models import *
from django.http import HttpResponse
from seller.models import*
# Create your views here.
def index (request):
    return render (request, 'customer/index.html')

def signup (request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # print(name,email,password)
        cust=Customer(name=name,email=email,password=password)
        cust.save()
        return redirect('customer:login')
    return render (request, 'customer/signup.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            cust=Customer.objects.get(email=email, password=password)
            request.session['customer']=cust.id
            return redirect('customer:products')
        except Customer.DoesNotExist:
            return render(request,'customer/login.html',{'msg':'invalid username or password'})



        # if Customer.objects.filter(email=email,password=password).exists():
        #     return HttpResponse('login successfully')
        # else:
        #     return render (request, 'customer/login.html', {'msg':'invalid email or password'})
    return render (request, 'customer/login.html')

def products(request):
    if 'customer' in request.session:
        products=Product.objects.all()
        return render(request, 'customer/products.html', {'products':products})
    else:
        return render(request, 'customer/index.html')       
        

def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return render (request, 'customer/login.html')
    else:
        return render(request, 'customer/index.html')   

def add_to_cart(request, product_id):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        if request.method=='POST':
            product=Product.objects.get(id=product_id)
            cart_item, created=Cart.objects.get_or_create(product=product, customer=cust)
            if not created:
                cart_item.quantity+=1
                cart_item.save()
            
    return redirect('customer:cart')   

def cart(request):
     if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        cart_items=Cart.objects.filter(customer=cust)
        total_price=sum(item.product.price*item.quantity for item in cart_items)
      

        return render(request, 'customer/cart.html', {'cart_items':cart_items,'total_price':total_price}) 
     else:
         return render (request, 'customer/index.html')
   
def remove_cart(request, product_id):
    if 'customer' in request.session:
        customer_id = request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        product=Product.objects.get(id=product_id)
        cart_item=Cart.objects.get(product=product, customer=cust)
        cart_item.delete()
        return redirect('customer:cart')

def pay_cart(request):
    return render (request, 'customer/payment.html')

def search(request):
 
 try:
    

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']

        if keyword:
            products=Product.objects.filter(description__icontains=keyword)
        context={
            'products':products,
        }

        
        
    return render(request, 'customer/products.html',context,)
 except:
    if 'customer' in request.session:
        products=Product.objects.all()
        return render(request, 'customer/products.html', {'products':products})
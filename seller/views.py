from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Seller,Product

# Create your views here.
def seller (request):

    if request.method=='POST':
        email= request.POST['email']
        password= request.POST['password']
        try:
            sell=Seller.objects.get(email=email, password=password)
            request.session['seller']=sell.id
            return redirect ('seller:dashboard')
        except Seller.DoesNotExist:
            return render (request, 'seller/seller.html', {'msg': 'invalid email or password'})
    return render (request, 'seller/seller.html')

def dashboard (request):
    if 'seller' in request.session:

        return render (request, 'seller/dashboard.html')
    else:
         return render (request, 'seller/seller.html')

def addproduct (request):

    if 'seller' in request.session:
    
        if request.method=='POST':
            name=request.POST['name']
            price=request.POST['price']
            description= request.POST['description']
            image=request.FILES['image']
            product= Product(name=name, price=price, description=description, image=image)
            product.save()
            return redirect('seller:dashboard')
        return render (request, 'seller/addproduct.html')
    else:
        return render (request,'seller/seller.html')

def viewproduct(request):
    if 'seller' in request.session:

        products=Product.objects.all()
        return render (request, 'seller/viewproduct.html',{'products':products})
    else:
        return render (request, 'seller/seller.html')

def signup(request):
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        password= request.POST['password']
        
        seller= Seller(name=name, email=email, password=password)
        seller.save()

        return redirect ('seller:seller')
        
        
    return render (request, 'seller/signup.html')



def delete_pdt(request, product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('seller:viewproduct')

def update_pdt(request, product_id):
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']

        try:
         description= request.POST['description']
         
        except:
            description=product.description
            
        try:
            image=request.FILES['image']
        except:
            image=product.image
            
            

        product.name=name
        product.price=price
        product.description=description
        product.image=image
        product.save()
        return redirect ('seller:viewproduct')
    return render (request, 'seller/update.html', {'product':product})

def logout (request):
    if 'seller' in request.session:
        del request.session['seller']
        return redirect('seller:seller')
    else:
        return render (request,'seller/seller.html')
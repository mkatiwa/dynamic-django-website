from django.shortcuts import render, redirect
from develop.models import product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def insert(request):
    return render(request, 'insert.html')

def insert(request):
    return render(request, 'insert.html')

def insertdata(request):
    if request.method == 'POST':
        prod_price = request.POST['prod_price']
        prod_name = request.POST['prod_name']
        prod_category = request.POST['prod_category']
        prod_qnty = request.POST['prod_qnty']
        prod_desc = request.POST['prod_desc']
        prod_img = request.FILES['prod_img']

        Product = product(
            prod_name=prod_name,
            prod_desc=prod_desc,
            prod_img=prod_img,
            prod_qnty=prod_qnty,
            prod_price=prod_price,
            prod_category=prod_category
                    )

        Product.save()
        return redirect('/')
    else:
        return render(request, 'insert.html')


def viewproducts(request):
    products = product.objects.all()
    return render(request, 'viewproducts.html', {"products": products})


def update(request, id):
    product = product.objects.get(id=id)
    if request.method == 'POST':
        prod_price = request.POST['prod_price']
        prod_name = request.POST['prod_name']
        prod_category = request.POST['prod_category']
        prod_qnty = request.POST['prod_qnty']
        prod_desc = request.POST['prod_desc']
        prod_img = request.FILES['prod_img']
        
        product.prod_name = prod_name
        product.prod_desc = prod_desc
        product.prod_img = prod_img
        product.prod_qnty = prod_qnty
        product.prod_price = prod_price
        product.prod_category = prod_category
        
        product.save()
        
        return redirect('/viewproducts')
    return render(request, 'update.html', {"product": product})

def delete_dt(request, id):
    product = product.objects.get(id=id)
    product.delete()
    return redirect('/viewproducts')
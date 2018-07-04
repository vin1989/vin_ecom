from django.shortcuts import render
from .forms import *
from .models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def index(request):
    category = Categories.objects.all()
    
    return render(request,'index.html',{'cat':category})

@login_required(login_url='/e_comm_login/')
def check_out(request):
    if request.method == 'POST':
        form = checkout_form(request.POST)
        #print request.POST
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = checkout_form()
    return render(request,'checkout.html',{'form':
                                           form})
def search(request):
    if request.method=="POST":
        
        s=request.POST.get('search')
        
        
        s = Product.objects.filter(name__icontains=s)
        if s:
            return render(request,'search.html',{'q':s})
        else:
            return render(request,'search.html',{'msg':'not found'})
            
            
    

def shop(request):
    category = Categories.objects.all()
    #print category
    default_category='chair'   #slug field for category(table)
    
    all_product = Product.objects.filter(category__slug='chair')
    #print all_product
    return render(request,'shop.html',{'cat':category,
                                       'pro':all_product,
                                       'd':default_category})

def Single_category(request,slug):
    category = Categories.objects.all()
    #print category
    
    all_product = Product.objects.filter(category__slug=slug)
    #print all_product
    return render(request,'shop_1.html',{'cat':category,
                                         'pro':all_product,
                                         'slug':slug})
def product_detail(request,d):
    product = Product.objects.get(id=d)
    if request.method=="POST":
        form = cart_form(request.POST)
        #print request.POST
        all_items = Cart.objects.all()
        cart_data={}
        for i in all_items:
            cart_data[i.product.id]={'product':i.product,
                                     'quantity':i.quantity}
        print cart_data
        q = request.POST['quantity']
        if form.is_valid():
            if int(d) in cart_data.keys():
                c = Cart.objects.get(product__id=d)
                c.quantity += int(q)
                
                c.total_price += float(c.product.price) * float(q)
                c.save()
            else:
                f=form.save(commit=False)
                f.product=product
                f.quantity=q
                f.total_price = float(product.price) * float(q)
                f.save()
            return HttpResponseRedirect('/cart_detail/')
    else:
        form = cart_form()
    return render(request,'product-details.html',{'detail':product,
                                                  'form':form})



def cart_detail(request):
    all_items = Cart.objects.all()
    '''
    d={}
    for i in all_items:
        d[i.product.id]={'product':i.product,
                         'quantity':i.quantity}
    print d
    '''
    total=[]
    for i in all_items:
        total.append(i.total_price)
    return render(request,'cart.html',{'all':all_items,
                                       'total':sum(total)})



def delete_item(request,d):
    item = Cart.objects.get(id=d)
    item.delete()
    return HttpResponseRedirect('/cart_detail/')




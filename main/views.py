from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClForm
from .models import Client, Product, Event
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request,'main.html')
def base(request):
    return render(request,'base.html')

def eventdetail(request, event_id): #views.py의 pk변수명과 urls.py의 변수명은 같아야 함
    event = get_object_or_404(Event, pk = event_id) #모델과 pk를 designer_id라고 부를거야
    return render(request, 'eventdetail.html',{'event':event})
    #값을 보낼거임

def event(request):
    event = Event.objects.all()
    return render(request,'event.html', {'event':event})

def product(request, store_id, menu_id): #product.html
    products = Client.objects.all()
    store = get_object_or_404(Product, pk = product_id)
    product_object = get_object_or_404(Product, pk=product_id)
    product = product_object.menu.split('\r\n')[menu_id - 1].split(':')[0]
    product_quantity = product_object.menu.split('\r\n')[menu_id - 1].split(':')[1]
    total = 0
    for price in products:
        total += price.price
    return render(request,'product.html', {'product':product,'products':products,'product':product,'product_quantity':product_quantity,'total':total})

def payment(request):
    return render(request,'payment.html')

def goods(request):
    return render(request,'goods.html')

def mypage(request):
    return render(request,'mypage.html')
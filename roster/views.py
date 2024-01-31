from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Duty, Order
from .forms import DutyForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    duty_count = Duty.objects.all().count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    
    context={
        'orders':orders,
        'form':form,
        'orders_count':orders_count,
        'workers_count':workers_count,
        'duty_count':duty_count,
    }
    return render(request, 'dashboard/index.html',context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    duty_count = Duty.objects.all().count()
    context = {
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'duty_count':duty_count,
    }
    return render(request, 'dashboard/staff.html',context)

def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context={
        'workers':workers
    }
    return render(request, 'dashboard/staff_detail.html',context)

@login_required(login_url='user-login')
def duty(request):
    items = Duty.objects.all()
    #items = duty.objects.raw('SQL CODE') For writing sql code instead of using the Object Relational mapping.
    duty_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method=="POST":
        form= DutyForm(request.POST)
        if form.is_valid():
            form.save()
            duty_name = form.cleaned_data.get('name')#gets the name from the form so and stores in variable duty_name
            messages.success(request, f'Duty for {duty_name} has been added')
            return redirect('dashboard-duty')
    else:
        form = DutyForm()    
    context={
        'items':items,
        'form':form,
        'duty_count':duty_count,
        'workers_count':workers_count,
        'orders_count':orders_count,
    }
    return render(request, 'dashboard/duty.html', context)

def duty_delete(request, pk):
    item= Duty.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-duty')
    context = {
        'item':item
    }
    return render(request, 'dashboard/duty_delete.html',context)

def duty_update(request, pk):
    item=Duty.objects.get(id=pk)
    if request.method=="POST":
        form = DutyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-duty')
    else:
        form = DutyForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/duty_update.html',context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    duty_count = Duty.objects.all().count()
    context={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'duty_count':duty_count,
    }
    return render(request, 'dashboard/order.html',context)

@login_required(login_url='user-login')
def logout_user(request):
    logout(request)
    return render(request,'user/logout.html')

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Duty, Order, Leave, Complains, Ward
from .forms import DutyForm, OrderForm, Leaveform, ComplainForm, WardForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    items = Duty.objects.all()
    duty_count = Duty.objects.all().count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    leave_count = Leave.objects.all().count()
    complain_count = Complains.objects.all().count
    rooms_count = Ward.objects.all().count()
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
        'items':items,
        'orders_count':orders_count,
        'workers_count':workers_count,
        'duty_count':duty_count,
        'leave_count':leave_count,
        'complain_count':complain_count,
        'room_count':rooms_count,
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

@login_required(login_url='user-login')
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


@login_required(login_url='user-login')
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
def ward(request):
    rooms = Ward.objects.all()
    if request.method == "POST":
        form = WardForm(request.POST)
        if form.is_valid():
            form.save()
            ward_name = form.cleaned_data.get('name')#gets the name from the form so and stores in variable duty_name
            messages.success(request, f' {ward_name} has been added')
            return redirect('dashboard-ward')
    else:
        form = WardForm()
    
    context= {
        'rooms':rooms,
        'form':form,
    }
    return render(request,'dashboard/ward.html',context )

@login_required(login_url='user-login')
def ward_delete(request, pk):
    room= Ward.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('dashboard-ward')
    context = {
        'room':room
    }
    return render(request, 'dashboard/ward_delete.html',context) 

@login_required(login_url='user-login')
def ward_update(request, pk):
    room=Ward.objects.get(id=pk)
    if request.method=="POST":
        form = WardForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('dashboard-ward')
    else:
        form = WardForm(instance=room)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/ward_update.html',context)

@login_required(login_url='user-login')
def leave(request):
    docs = Leave.objects.all()
    #items = duty.objects.raw('SQL CODE') For writing sql code instead of using the Object Relational mapping.
    leave_count = docs.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method=="POST":
        form= Leaveform(request.POST)
        if form.is_valid():
            form.save()
            leave_name = form.cleaned_data.get('name')#gets the name from the form so and stores in variable duty_name
            messages.success(request, f'{leave_name}, your leave request has been sent.')
            return redirect('dashboard-index')
    else:
        form = Leaveform()    
    context={
        'docs':docs,
        'form':form,
        'leave_count':leave_count,
        'workers_count':workers_count,
        'orders_count':orders_count,
    }
    return render(request, 'dashboard/leave.html', context)

@login_required(login_url='user-login')
def leavelist(request):
    leaves = Leave.objects.all()
    leave_count = leaves.count()
    context = {
        'leaves':leaves,
        'leave_count':leave_count,
    }
    return render(request, "dashboard/leavelist.html",context)

@login_required(login_url='user-login') 
def leavesview(request,pk):
     leaveview = Leave.objects.get(id=pk)
     context ={
         'leaveview':leaveview,
     }
     return render(request,'dashboard/leavesview.html',context)


@login_required(login_url='user-login')
def complain(request):
    complain = Complains.objects.all()
    #items = duty.objects.raw('SQL CODE') For writing sql code instead of using the Object Relational mapping.
    complain_count = complain.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method=="POST":
        form= ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            complain_name = form.cleaned_data.get('name')#gets the name from the form so and stores in variable duty_name
            messages.success(request, f'{complain_name}, your complain has been sent for review.')
            return redirect('dashboard-index')
    else:
        form = ComplainForm()    
    context={
        'complain':complain,
        'form':form,
        'complain_count':complain_count,
        'workers_count':workers_count,
        'orders_count':orders_count,
    }
    return render(request, 'dashboard/complain.html', context)

@login_required(login_url='user-login')
def complainlist(request):
    complains = Complains.objects.all()
    complain_count = complains.count()
    context = {
        'complains':complains,
        'complain_count':complain_count,
    }
    return render(request, "dashboard/complain_list.html",context)



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

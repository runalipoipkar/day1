from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginPage_url')
def order_view(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name='app1/addorder.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='loginPage.html')
def show_view(request):
    data=Order.objects.all()
    template_name='app1/Show.html'
    context={'data':data}
    return render(request, template_name, context)


def update_view(request,pk):
    obj=Order.objects.get(id=pk)
    form=OrderForm(instance=obj)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name='app1/addorder.html'
    context={'form':form}
    return render(request, template_name, context)


def delete_view(request,pk):
    obj=Order.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('show_url')
    template_name='app1/delete_confirmation.html'
    context={'data':obj}
    return render(request, template_name, context)

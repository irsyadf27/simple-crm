from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.views.generic import View
from .models import Products, Editions
from .forms import CreateForm

# Create your views here.

class ProductsCreateView(CreateView):
    model = Products
    template_name = 'products/products_create.html'
    fields = ['name', 'sku', 'vendor', 'price_per', 'price', 'monthly_price', 'yearly_price', 'tags', 'description', ]

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            test = product.save()

            pairs = zip(request.POST.getlist('editions_name'), request.POST.getlist('editions_perpetual'), request.POST.getlist('editions_monthly_price'), request.POST.getlist('editions_yearly_price'))

            for e_name, e_perpetual, e_monthly, e_yearly in pairs:
                if e_name is not '':
                    e = Editions(
                        product=test.id, name=e_name, perpetual=e_perpetual,
                        monthly_price=e_monthly, yearly_price=e_yearly
                        )
                    e.save()
            return redirect('home')
    else:
        form = CreateForm()
    return render(request, 'products/create.html', {'form': form})

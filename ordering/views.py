from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, order, company, profile
from .forms import ProductForm
from django.utils.translation import gettext as _
# Create your views here.
@login_required
def get_products(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'index.html', {'products': products, 'user': request.user.profile})
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if request.user.profile.role != 'operator':
            return HttpResponse("You are viewer, You are not authorized to create an order.", status=403)
        else:
            if form.is_valid():
                product = form.save(commit=False)
                product.created_by = request.user
                product.company = request.user.profile.company
                product.save()
                return HttpResponse("Product added successfully.", status=201)
            else:
                form = ProductForm()
                return render(request, 'index.html', {'form': form, 'products': products, 'user': request.user.profile})
    else:
        products = Product.objects.filter(is_active=True)
        form = ProductForm()
        if request.user.profile.role != 'operator':
            return HttpResponse("You are viewer, You are not authorized to create an order.", status=403)
        return render(request, 'index.html', {'form': form, 'products': products, 'user': request.user.profile})
@login_required
def create_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        if product.is_active is False:
            return HttpResponse("Product is not available for ordering.", status=400)
        if product.stock <= 0:
            return HttpResponse("Product is out of stock.", status=400)
        if quantity > product.stock:
            return HttpResponse("Insufficient stock for the requested quantity.", status=400)
        if request.user.profile.role != 'operator':
            return HttpResponse("You are viewer, You are not authorized to create an order.", status=403)
        if product.stock >= quantity:
            product.stock -= quantity
            product.save()
        new_order = order.objects.create(
            company=product.company,
            created_by=request.user,
            created_at=order.created_at,
            status='pending',
            Product_name=product,
            quantity=quantity
        )
        orders = order.objects.all()
        action = 'created'
        return render(request, 'orders.html', {'order': new_order, 'orders': orders, 'action': action})
    else:
        orders = order.objects.all()
        orders = orders.filter(created_by=request.user)
        action = 'viewed'
        return render(request, 'orders.html', {'orders': orders, 'action': action})
@login_required 
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.created_by == request.user and request.user.profile.role == 'operator':
        product.is_active = False
        product.is_deleted = True
        product.save()
        return HttpResponse("Product deleted successfully.", status=200)
    else:
        return HttpResponse("You are not authorized to delete this product.", status=403)
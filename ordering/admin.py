from django.contrib import admin
from .models import Product, order, company, profile

admin.site.site_header = 'Poultry Task Admin'
admin.site.site_title = 'Poultry Task Admin'
admin.site.index_title = 'Welcome to Poultry Task Admin'
admin.site.register(company)
admin.site.register(profile)

@admin.action(description='Mark selected products as inactive')
def mark_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'company', 'created_by', 'created_at', 'last_updated_at')
    fields = ('name', 'price', 'stock', 'is_active')
    list_filter = ('is_active',)
    actions = [mark_inactive]
    search_fields = ('name', 'company__name')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.profile.user
            obj.company = request.user.profile.company
        obj.save()
    def has_add_permission(self, request):
        return request.user.is_authenticated and request.user.is_superuser and request.user.profile.role == 'operator'

import pandas as pd
from django.http import HttpResponse
@admin.action(description='Export selected orders to CSV')
def export_to_csv(modeladmin, request, queryset):
    orders_data = queryset.values('id', 'company__name', 'created_by__user__username', 'created_at', 'status', 'Product_name__name', 'quantity')
    df = pd.DataFrame(list(orders_data))
    csv_file = df.to_csv(index=False)
    
    response = HttpResponse(csv_file, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    return response
@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'created_by', 'created_at', 'status', 'Product_name', 'quantity')
    fields = ('company', 'status', 'Product_name', 'quantity')
    actions = [export_to_csv]
    search_fields = ('company__name', 'Product_name__name')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.profile.user
            obj.company = request.user.profile.company
        obj.save()
    def has_add_permission(self, request): 
        return request.user.is_authenticated and request.user.is_superuser and request.user.profile.role == 'operator'
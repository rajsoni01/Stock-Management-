from django.contrib import admin
from.models import *
# Register your models here.

admin.site.register(add_party)

admin.site.register(item_category)

admin.site.register(items)

# admin.site.register(purchase_bill)

# admin.site.register(purchase_items)



class PurchaseItemsInline(admin.TabularInline):
    model = purchase_items
    extra = 1  # Number of empty forms to display
    readonly_fields = ['amount']  # Optional: make 'amount' read-only

@admin.register(purchase_bill)
class PurchaseBillAdmin(admin.ModelAdmin):
    list_display = ['Entry_no', 'party_name', 'date', 'time', 'total_qty', 'total_amount', 'paid_amount', 'due_amount']
    search_fields = ['party_name', 'Entry_no']
    list_filter = ['date']
    inlines = [PurchaseItemsInline]  # Show items inline with bill

@admin.register(purchase_items)
class PurchaseItemsAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity', 'purchase_price', 'amount', 'bill']
    search_fields = ['item_name', 'bill__Entry_no']
    list_filter = ['bill__date']

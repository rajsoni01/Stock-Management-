from django.db import models

# Create your models here.

class add_party(models.Model):
    party_name=models.CharField(max_length=50)
    number= models.BigIntegerField(null=True, blank=True, default="null")
    opening_balance= models.IntegerField(null=True)
    party_type=models.CharField(max_length=20)
    GST_no=models.CharField(max_length=100, null=True, blank=True)
    PAN_no=models.BigIntegerField(null=True, blank=True)
    billing_add=models.CharField(max_length=200, blank=True, null=True)
    billing_pin=models.IntegerField(null=True, blank=True)
    billing_state=models.CharField(max_length=100, null=True, blank=True)
    account_holder_name=models.CharField(max_length=100, blank=True, null=True)
    bank_name=models.CharField(max_length=100, blank=True, null=True)
    account_number=models.BigIntegerField(null=True, blank=True)
    IFSC_code=models.CharField(max_length=50, null=True, blank=True)
    branch_name=models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.party_name
    

class item_category(models.Model):
    category_name=models.CharField(max_length=100)
    category_description=models.TextField(max_length=300,blank=True, null=True)
    def __str__(self):
        return self.category_name
    

class items(models.Model):
    item_name=models.CharField(max_length=50, null=True, blank= True)
    purchase_price=models.IntegerField(null=True, blank= True)
    purchase_gst=models.CharField(max_length=50, null=True, blank= True)
    mrp=models.IntegerField(null=True, blank= True)
    selling_price=models.IntegerField(null=True, blank= True)
    selling_gst=models.CharField(max_length=50, null=True, blank= True)
    unit=models.CharField(max_length=50)
    hsn_code=models.CharField(max_length=100, null=True, blank=True)
    gst_rate=models.CharField(max_length=50)
    low_stock=models.IntegerField(null=True, blank= True)
    category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.item_name



    


class purchase_bill(models.Model):
    party_name = models.CharField(max_length=50)
    Entry_no = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    total_qty=models.IntegerField()
    total_amount = models.BigIntegerField()
    paid_amount = models.BigIntegerField()  # ✅ Changed from BigAutoField to BigIntegerField
    due_amount = models.BigIntegerField()

    def __str__(self):
        return self.party_name
    
    
class purchase_items(models.Model):  # ✅ Fixed typo (it was "purchase_itmes")
    bill = models.ForeignKey(purchase_bill, on_delete=models.CASCADE, related_name="items")  #Django understands "items" as the set of PurchaseItems linked to each PurchaseBill.


    item_name = models.CharField(max_length=50, null=True, blank=True)
    description= models.CharField(max_length=200)
    quantity = models.IntegerField()
    purchase_price = models.BigIntegerField()  # ✅ Fixed inconsistent naming
    amount = models.BigIntegerField()

    def __str__(self):
        return f"{self.item_name} (x{self.quantity}) - Bill {self.bill.Entry_no}"


# this is for only working test






# class purchase_bill(models.Model):
#     party_name = models.CharField(max_length=50)
#     Entry_no = models.CharField(max_length=20)
#     date = models.DateField()
#     time = models.TimeField()
#     total_qty=models.IntegerField(default=0)
#     total_amount = models.BigIntegerField(default=0)
#     paid_amount = models.BigIntegerField(default=0)  # ✅ Changed from BigAutoField to BigIntegerField
#     due_amount = models.BigIntegerField(default=0)
    
#     #purcahse item
    
#     item_name = models.CharField(max_length=50, null=True, blank=True)
#     description= models.CharField(max_length=200, null=True, blank=True)
#     quantity = models.IntegerField(default=0)
#     purchase_price = models.BigIntegerField(default=0)  # ✅ Fixed inconsistent naming
#     amount = models.BigIntegerField(default=0)

#     def __str__(self):
#         return self.party_name
    
    

from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from.models import *

# Create your views here.

def party(request):
    
    # to_pay=add_party.objects.exclude(party_type='To Pay')
    # to_receive=add_party.objects.exclude(party_type='To Receive')
    
    
    party_data=add_party.objects.all()
    
    
    
    return render(request, "party.html",{"party_data":party_data})


def Add_party(request):
    if request.method=="POST":
        p_name=request.POST.get("party_name")
        mobile_no=request.POST.get("mobile_number")
        opening_bal=request.POST.get("opening_balance")
        party_typ=request.POST.get("party_type")
        gst_no=request.POST.get("gst_number")
        pan_no=request.POST.get("pan_number")
        billing_add=request.POST.get("billing_address")
        billing_zip_code=request.POST.get("billing_pincode")
        billing_state=request.POST.get("billing_state")
        acc_holdername=request.POST.get("acc_holder_name")
        bank_name=request.POST.get("bank_name")
        account_no=request.POST.get("acc_number")
        ifsc=request.POST.get("ifsc_code")
        branch_name=request.POST.get("branch_name")
        
        
        party=add_party(party_name=p_name, number=mobile_no, opening_balance=opening_bal, party_type=party_typ, GST_no=gst_no, PAN_no=pan_no, billing_add=billing_add, billing_pin=billing_zip_code, billing_state=billing_state, account_holder_name=acc_holdername, bank_name=bank_name, account_number=account_no, IFSC_code=ifsc, branch_name=branch_name )
        party.save()
        
        
        return redirect("/")
        
        
        
    return render(request, "add_party.html")


def delete_party(request,id):
    dele = add_party.objects.filter(id=id)
    dele.delete()
    return redirect ('/')


def update_party(request,id):
    party = add_party.objects.get(id=id)
    
    
    if request.method=="POST":
        p_name=request.POST.get("party_name")
        mobile_no=request.POST.get("mobile_number")
        opening_bal=request.POST.get("opening_balance")
        party_type=request.POST.get("party_type")
        gst_no=request.POST.get("gst_number")
        pan_no=request.POST.get("pan_number")
        billing_add=request.POST.get("billing_address")
        billing_zip_code=request.POST.get("billing_pincode")
        billing_state=request.POST.get("billing_state")
        acc_holdername=request.POST.get("acc_holder_name")
        bank_name=request.POST.get("bank_name")
        account_no=request.POST.get("acc_number")
        ifsc=request.POST.get("ifsc_code")
        branch_name=request.POST.get("branch_name")
        
          
        
        party.party_name=p_name
        party.number=mobile_no
        party.opening_balance=opening_bal
        party.party_type=party_type
        party.GST_no=gst_no
        party.PAN_no=pan_no
        party.billing_add=billing_add
        party.billing_pin=billing_zip_code
        party.billing_state=billing_state
        party.account_holder_name=acc_holdername
        party.bank_name=bank_name
        party.account_holder_name=account_no
        party.IFSC_code=ifsc
        party.branch_name=branch_name
        
        party.save()
        
        return redirect("/")
    
    
    
    
    return render(request, "update_party.html",{"party":party})



def items_category(request):
    

    if request.method=="POST":
        cate_name=request.POST.get("category_name")
        cate_description=request.POST.get("category_description")
        
        item_cate=item_category(category_name=cate_name, category_description=cate_description)
        item_cate.save()
    category=item_category.objects.all()
        
    return render(request, "item_category.html", {"category":category})

def delete_items_category(request,id):
    dele = get_object_or_404(item_category, id=id)
    dele.delete()
    return redirect ('/item_category')


def update_items_category(request,id):
    item_cate=get_object_or_404(item_category, id=id)
    
    if request.method=="POST":
        cate_name=request.POST.get("category_name")
        cate_description=request.POST.get("category_description")
        
        
        item_cate.category_name=cate_name
        item_cate.category_description=cate_description
        item_cate.save()
        
        
        return redirect('/item_category')
    
    return render(request, "update_item_category.html", {"cate":item_cate})

        
def item(request):
    item_data=items.objects.all()
    
    
    
    
    return render(request,"item.html", {"item":item_data})



def add_items(request):
    cate=item_category.objects.all()
    
    
    if request.method=="POST":
        item_name=request.POST.get("item_name")
        purchase_price=request.POST.get("purchase_price")
        purchase_gst=request.POST.get("purchase_gst")
        mrp=request.POST.get("mrp")
        selling_price=request.POST.get("selling_price")
        selling_gst=request.POST.get("selling_gst")
        unit=request.POST.get("unit")
        hsn_code=request.POST.get("hsn_code")
        gst_rate=request.POST.get("gst_rate")
        low_quantity=request.POST.get("low_quantity")
        category=request.POST.get("category")
        
        items_data=items(item_name=item_name, purchase_price=purchase_price,purchase_gst=purchase_gst, mrp=mrp, selling_price=selling_price, selling_gst=selling_gst, unit=unit, hsn_code=hsn_code, gst_rate=gst_rate, low_stock=low_quantity, category=category)
        items_data.save()
        
        return redirect("/items")
    


    return render(request,"add_item.html", {"category":cate})


def delete_item(request,id):
    dele = get_object_or_404(items, id=id)
    dele.delete()
    return redirect ('/items')


def update_items(request):
    cate=item_category.objects.all()
    
    
    if request.method=="POST":
        item_name=request.POST.get("item_name")
        purchase_price=request.POST.get("purchase_price")
        purchase_gst=request.POST.get("purchase_gst")
        mrp=request.POST.get("mrp")
        selling_price=request.POST.get("selling_price")
        selling_gst=request.POST.get("selling_gst")
        unit=request.POST.get("u    nit")
        hsn_code=request.POST.get("hsn_code")
        gst_rate=request.POST.get("gst_rate")
        low_quantity=request.POST.get("low_quantity")
        category=request.POST.get("category")
        
        items_data=items(item_name=item_name, purchase_price=purchase_price,purchase_gst=purchase_gst, mrp=mrp, selling_price=selling_price, selling_gst=selling_gst, unit=unit, hsn_code=hsn_code, gst_rate=gst_rate, low_stock=low_quantity, category=category)
        items_data.save()
        
        return redirect("/items")
    


    return render(request,"item_update.html")

def stock(request):
    item=items.objects.all()
    return render(request, "stock.html",{"item":item})

def add_purchase(request):
    if request.method=="POST":
        party_name=request.POST.get("party")
        enrty_no=request.POST.get("entry_no")
        date=request.POST.get("date")
        time=request.POST.get("time")
        
        
        #summary
        
        total_qty=request.POST.get("total_qty")
        total_amount=int(request.POST.get("total_amount").replace("Rs. ", ""))
        paid_amount=request.POST.get("paid_amount")
        due_amount=int(request.POST.get("due_amount").replace("Rs. ", ""))
        
        purchase_data=purchase_bill.objects.create(
            party_name=party_name,
            Entry_no=enrty_no, 
            date=date, time=time, 
            total_qty=total_qty, 
            total_amount=total_amount, 
            paid_amount=paid_amount, 
            due_amount=due_amount)
        
        
        
        
        #items entry
        item_name=request.POST.getlist("item []")
        item_description=request.POST.getlist("description []")
        item_qty=request.POST.getlist("item_qty []")
        item_price=request.POST.getlist("item_price []")
        item_total_price=request.POST.getlist("item_total_price []")
        
        for i in range(len(item_name)):
            purchase_items.objects.create(
                
                bill=purchase_data,
                item_name=item_name[i],
                description=item_description[i],
                quantity=int(item_qty[i]),
                purcahse_price=int(item_price[i]),
                amount=int(item_total_price[i].replace("Rs. ", ""))
                )
            
            
            # item_names = item_name[i]
            # description = item_description[i]
            # item_quantity = (item_qty[i])
            # purchase_price = (item_price[i])
            # items_total_amounts = int(item_total_price[i].replace("Rs. ", ""))

        
            # purchase_item=purchase_items.objects.create(
            #     bill=purchase_data,  # foreign key relation
            #     item_name=item_names, 
            #     description=description, 
            #     quantity=item_quantity,
            #     purchase_price=purchase_price, 
            #     amount=items_total_amounts
            #     )
            
        
        
      
        
        
        
        return redirect("/purchase")
    

        
        
    item_data=items.objects.all()
    party_data=add_party.objects.all()
    
    return render(request, "purchase_add.html", {"party":party_data, "product":item_data})


def update_purchase_bill(request, id):
    purchasebills=purchase_bill.objects.prefetch_related("items").get(id=id)
    item_data=items.objects.all()
    party_data=add_party.objects.all()



    # purchasebills= purchase_bill.objects.prefetch_related("items").all()
    
    return render(request, "update_purchase_bill.html", {"purchase_data": purchasebills, "product":item_data, "party":party_data})



def purchase(request):
    purchase=purchase_bill.objects.all()
    
    return render(request, "purchase.html", {"purchase_data":purchase})
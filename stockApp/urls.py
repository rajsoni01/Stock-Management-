"""
URL configuration for stock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from.views import *


urlpatterns = [
    path("",party),
    path("add",Add_party),
    path("delete_party/<int:id>", delete_party),
    path("update_party/<int:id>", update_party),
    
    path("items",item),
    path("add_items",add_items),
    path("delete_item/<int:id>", delete_item),
    path("update_item",update_items),
    
    path("item_category", items_category),
    path("delete_item_category/<int:id>", delete_items_category),
    path( "update_item_category/<int:id>", update_items_category),
    
    
    path("item_stock", stock),
    
    
    path("add_purchase", add_purchase),
    path("purchase", purchase),
    path("view_purchase/<int:id>", update_purchase_bill)

]
    
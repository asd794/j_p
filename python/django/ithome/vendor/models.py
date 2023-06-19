from typing import Any, List, Tuple
from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name=models.CharField(max_length=20) # 攤販的名稱
    store_name=models.CharField(max_length=10) # 攤販店家的名稱
    phone_number=models.CharField(max_length=20) # 攤販的電話號碼
    address=models.CharField(max_length=100) # 攤販的地址
    # primary_key=True
    
    def __str__(self):
        return self.vendor_name # 去資料庫查資料原本回傳<Vendor: Vendor object (1)> 變成 <Vendor: Alex>


class Food(models.Model):
    food_name = models.CharField(max_length=30) # 食物名稱
    price_name=models.DecimalField(max_digits=3,decimal_places=0) # 食物價錢
    food_vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的

    def __str__(self):
        return self.food_name

from django.contrib import admin

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']

from django.utils.translation import gettext_lazy as _
class Morethanfifty(admin.SimpleListFilter):
    title=_('price')
    parameter_name='compareprice'
    def lookups(self, request: Any, model_admin):
        return (('>50',_('>50')),('<=50',_('<=50')),)
    def queryset(self, request, queryset):
        if self.value() == '>50':
            return queryset.filter(price_name__gt=50)
        if self.value() == '<=50':
            return queryset.filter(price_name__lte=50)
              
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    # list_display = ['id', 'food_name', 'price_name', 'food_vendor'] # 等於上面那行
    list_filter=(Morethanfifty,) # 過濾 price_name
    # fields=['price_name'] # 只能修改 price_name # 等於 exclude=['food_name', 'food_vendor']
    search_fields=('food_name','price_name') # 搜尋欄位
    ordering=('price_name',) # 預設顯示價格小到大排序 # 大到小 ordering = ('-price_name',)


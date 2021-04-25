from django.contrib import admin
from .models import CementPrice,Supply,Supplier,Stock,Labour,LabourTypes,\
    LabourWorkTime,CostEstimation,ConstructionSite,Client,SiteManageger,\
    StockManagement,Invoice,Author,LabourRequest,SuppluStockUpdate,Material,SteelPrice,BricksPrice,AggregatePrice,SandPrice,FlooringPrice,PaintingPrice,SanitaryFittingsPrice,ElectricFittingPrice


# Register your models here.

admin.site.register(Author)
admin.site.register(Supply)
admin.site.register(Supplier)
admin.site.register(Stock)
admin.site.register(Labour)
admin.site.register(LabourTypes)
admin.site.register(LabourWorkTime)
admin.site.register(ConstructionSite)
admin.site.register(StockManagement)
admin.site.register(Invoice)
admin.site.register(Material)
admin.site.register(Client)
admin.site.register(SiteManageger)
admin.site.register(CostEstimation)
admin.site.register(CementPrice)

admin.site.register(SteelPrice)
admin.site.register(BricksPrice)
admin.site.register(AggregatePrice)
admin.site.register(SandPrice)
admin.site.register(FlooringPrice)
admin.site.register(PaintingPrice)
admin.site.register(SanitaryFittingsPrice)
admin.site.register(ElectricFittingPrice)
admin.site.register(SuppluStockUpdate)
admin.site.register(LabourRequest)








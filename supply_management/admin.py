from django.contrib import admin
from .models import Supply,Supplier,Stock,Labour,LabourTypes,LabourWorkTime,ConstructionSite,Client,SiteManageger,StockManagement,Invoice,Material

# Register your models here.

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



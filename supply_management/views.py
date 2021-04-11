from django.db.models import Sum
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.base import View

from .models import Supply, Supplier, Stock,Material,Labour,LabourTypes,StockManagement,ConstructionSite,LabourWorkTime


# Create your views here.



def supply_add(request):
    obj = Supplier.objects.all()
    material = Material.objects.all()
    context={
        "obj":obj,
        "material":material,
        "isact_supply":"active",
    }
    if request.method =="POST":
        supplier_company_name = request.POST.get("supplier_company_name")
        supplier_company_obj = Supplier.objects.get(name=supplier_company_name)
        material_obj = request.POST.get("material")
        material = Material.objects.get(material_name=material_obj)
        lot_no = request.POST.get("lot_no")
        quantity = request.POST.get("quantity")
        unit_price = request.POST.get("unit_price")
        obj = Supply(supplier_company_name=supplier_company_obj,lot_no=lot_no,quantity=quantity,unit_price=unit_price,material=material)
        obj.save()
        messages.success(request, "Successfully Added To List")
        return redirect('list')
    return render(request, "supply_management/supply_add.html", context)


def supply_list(request):
    obj = Supply.objects.all()
    context={
        "obj":obj,
        "isact_supply": "active",
    }
    return render(request, "supply_management/supply_list.html", context)


def supply_view(request, id):
    obj = get_object_or_404(Supply, id=id)
    context={
        "obj":obj,
        "isact_supply": "active",
    }
    return render(request, "supply_management/supply_view.html", context)


def supply_update(request, id):
    supplier_obj = Supplier.objects.all()
    obj = get_object_or_404(Supply, id=id)
    context={
        "obj":obj,
        "supplier_obj":supplier_obj,
        "isact_supply": "active",
    }
    if request.method == "POST":
        supplier_company = request.POST.get("supplier_company_name")
        get_supplier = Supplier.objects.get(name=supplier_company)
        obj.supplier_company_name = get_supplier
        obj.lot_no = request.POST.get("lot_no")
        obj.quantity = request.POST.get("quantity")
        obj.unit_price = request.POST.get("unit_price")
        obj.save()
        messages.success(request, "Supply Update Successfully")
        return redirect('list')
    return render(request, "supply_management/supply_update.html", context)
#
#
def supply_remove(request, id):
    obj = get_object_or_404(Supply, id=id)
    obj.delete()
    messages.success(request, "Supply Delete Successfully")
    return redirect('list')


def add_supplier(request):
    sup_obj = Supplier.objects.all()[::-1]
    context={
        "supplier":sup_obj,
        "isact_supplier": "active",
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        comments = request.POST.get("comments")
        obj = Supplier(name=name,email=email,phone=phone,address=address,comments=comments)
        obj.save()
        messages.success(request, "supplier Added Successfully ")
        return redirect('add_supplier')
    return render(request, "supply_management/add_new_supplier.html", context)


def update_supplier(request, id):
    supplier_obj = get_object_or_404(Supplier, id=id)
    context={
        "supplier":supplier_obj
    }
    if request.method == "POST":
        supplier_obj.name = request.POST.get("name")
        supplier_obj.email = request.POST.get("email")
        supplier_obj.phone = request.POST.get("phone")
        supplier_obj.address = request.POST.get("address")
        supplier_obj.comments = request.POST.get("comments")
        supplier_obj.save()
        messages.success(request, "Supplier Update Successfully")
        return redirect('add_supplier')
    return render(request, "supply_management/supplier_update.html", context)


def remove_supplier(request, id):
    obj = get_object_or_404(Supplier, id=id)
    obj.delete()
    messages.success(request, "Supplier Removed Successfully")
    return redirect('add_supplier')


def labour_type(request):
    labour_type_obj = LabourTypes.objects.all()[::-1]
    context={
        "labour_type":labour_type_obj
    }
    if request.method == "POST":
        labour_types = request.POST.get("labour_types")
        obj = LabourTypes(labour_types=labour_types)
        obj.save()
        messages.success(request, "Labour Type Added Successfully")
        return redirect('labour_type')
    return render(request, "labour/labour_type_list.html", context)


def update_labour_type(request, id):
    obj = get_object_or_404(LabourTypes, id=id)
    if request.method == "POST":
        obj.labour_types = request.POST.get("labour_types")
        obj.save()
        messages.success(request, "Labour Type Update Successfully")
        return redirect('labour_type')



def remove_labour_type(request, id):
    obj = get_object_or_404(LabourTypes, id=id)
    obj.delete()
    messages.success(request, "Labour Type Remove Successfully")
    return redirect('labour_type')


def labour_list(request):
    labour_obj = Labour.objects.all()[::-1]
    context={
        "labour": labour_obj,
        'isact_labourlist': 'active'
    }
    return render(request, "labour/labour_list.html", context)


def add_new_labour(request):
    labour_type = LabourTypes.objects.all()
    context={
        'labour_type':labour_type,
        'isact_labourlist':'active'
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        lab = request.POST.get("labour_type")
        labour_t = LabourTypes.objects.get(id=int(lab))
        qualification = request.POST.get("qualification")
        nid_number = request.POST.get("nid_number")
        photo = request.FILES.get("photo")
        obj = Labour(labour_type=labour_t,name=name, phone=phone, address=address, qualification=qualification, nid_number=nid_number,photo=photo)
        obj.save()
        messages.success(request, "Labour added successfully")
        return redirect('labour_list')
    return render(request, "labour/add_new_labour.html", context)


def work_time_list(request):
    obj = LabourWorkTime.objects.all()
    context={
        "obj":obj
    }
    return render(request, "labour/work_time_list.html", context)


def add_labour_work_time(request):
    cons_site = ConstructionSite.objects.all()
    lab = Labour.objects.all()
    context={
        "cons_site":cons_site,
        "lab":lab
    }
    if request.method == "POST":
        consturction_site_obj = request.POST.get("consturction_site")
        consturction_site = ConstructionSite.objects.get(location=consturction_site_obj)
        labour_obj = request.POST.get("labour")
        labour = Labour.objects.get(name=labour_obj)
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        work_time_obj = LabourWorkTime(consturction_site=consturction_site,labour=labour,start_date=start_date,end_date=end_date)
        work_time_obj.save()
        messages.success(request, "Labour Work Time Added Successfully")
        return redirect("work_time_list")
    return render(request, "labour/add_labour_work_time.html", context)

def labour_update(request, id):
    obj = get_object_or_404(Labour, id=id)
    type = LabourTypes.objects.all()
    context={
        "labour":obj,
        "type":type,
        'isact_labourlist': 'active'
    }
    if request.method == "POST":
        obj.name = request.POST.get("name")
        obj.phone = request.POST.get("phone")
        obj.address = request.POST.get("address")
        labour_type = request.POST.get("labour_type")
        obj.type = LabourTypes.objects.get(labour_types=labour_type)
        obj.qualification = request.POST.get("qualification")
        obj.nid_number = request.POST.get("nid_number")
        if request.FILES.get("photo"):
            obj.photo = request.POST.get("photo")
        obj.save()
        messages.success(request, "Labour Update Successfully!!")
        return redirect('labour_list')
    return render(request, "labour/update_labour.html", context)


def remove_labour(request, id):
    obj = get_object_or_404(Labour, id=id)
    obj.delete()
    messages.success(request, "Labour removed successfully")
    return redirect('labour_list')


def stock_list(request):
    obj = Stock.objects.all()[::-1]
    stock_obj = Stock.objects.all()
    total_quantity = stock_obj.aggregate(Sum('quantity'))['quantity__sum']
    context={
        "obj":obj,
        "isact_stocklist":"active",
        "total_quantity":total_quantity
    }
    return render(request, "stock/stock_list.html",context)


def add_new_stock(request):
    obj = Material.objects.all()
    context={
        "obj":obj,
        "isact_stocklist": "active",
    }
    if request.method == "POST":
        material_obj = request.POST.get("material")
        material = Material.objects.get(material_name=material_obj)
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        update_by = request.user
        stock_obj = Stock(name=name,material=material,quantity=quantity,update_by=update_by)
        stock_obj.save()
        messages.success(request, "Stock Added Successfully")
        return redirect('stock_list')
    return render(request, "stock/add_new_stock.html", context)


def stock_management(request):
    obj = StockManagement.objects.all()
    context={
        "obj":obj,
        "isact_stockmanagement":"active"
    }
    return render(request, "stock/stock_management.html", context)


def add_stock_management(request):
    obj = ConstructionSite.objects.all()
    material_obj = Material.objects.all()
    if request.method == "POST":
        construct_site_obj = request.POST.get("construct_site")
        construct_site = ConstructionSite.objects.get(location=construct_site_obj)
        mat_obj = request.POST.get("material")
        material = Material.objects.get(material_name=mat_obj)
        quantity = request.POST.get("quantity")
        stock_management_obj = StockManagement(construct_site=construct_site,material=material,quantity=quantity)
        stock_management_obj.save()
        messages.success(request, "Added Successfully")
        return redirect('stock_management')
    context={
        "isact_stockmanagement": "active",
        "material_obj":material_obj,
        "obj":obj
    }
    return render(request, "stock/add_new_stock_management.html", context)



# def stock_list(request):
#     obj = Stock.objects.all()[::-1]
#     stock_obj = Stock.objects.all()
#     total_quantity = stock_obj.aggregate(Sum('quantity'))['quantity__sum']
#     site_obj = SiteManageger.objects.filter(is_approve=True)
#     total_quantity_site = site_obj.aggregate(Sum('quantity'))['quantity__sum']
#     if total_quantity_site is None :
#         total_quantity_site = 0
#     elif total_quantity is None:
#         total_quantity =0
#     total =int(total_quantity)-int(total_quantity_site)
#
#     context={
#         "obj":obj,
#         "total":int(total),
#         "total_quantity":int(total_quantity),
#         "total_quantity_site":total_quantity_site,
#         "isact_stock": "active",
#     }
#     return render(request, "stock/stock_list.html", context)
#
#

#
#
# def site_manager_request_list(request, filter):
#     obj = None
#     if filter == 'None':
#         obj = SiteManageger.objects.all()[::-1]
#     elif filter == 'Approved':
#         obj = SiteManageger.objects.all().filter(is_approve=True)[::-1]
#     elif filter == 'Pending':
#         obj = SiteManageger.objects.all().filter(is_approve=False)[::-1]
#
#     site_obj = SiteManageger.objects.filter(is_approve=True)
#     total_quantity = site_obj.aggregate(Sum('quantity'))['quantity__sum']
#     context = {
#         "obj":obj,
#         'total_required_quantity': total_quantity,
#         "isact_site_manager": "active",
#     }
#     return render(request, "stock/site_manager_request_list.html", context)
#
#
# def site_manager_request(request):
#     if request.method == "POST":
#         category = request.POST.get("category")
#         material = request.POST.get("material")
#         quantity = request.POST.get("quantity")
#         manager_obj = SiteManageger(category=category, material=material, quantity=quantity, site_manager=request.user)
#         manager_obj.save()
#         messages.success(request, "Your Request Send to our Admin, Please Wait for his approval")
#         return redirect('site_manager_request_list', filter='None')
#     context={
#         "isact_site_manager": "active",
#     }
#     return render(request, "stock/site_manager_request.html", context)
#
#
# def site_manager_request_delete(request, id):
#     obj = get_object_or_404(SiteManageger, id=id)
#     obj.delete()
#     messages.success(request, "Successfully Remove")
#     return redirect('site_manager_request_list', filter='None')
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from sadmin.models import Notification
# for Pdf views
# for pff import 
from io import BytesIO
from django.views import View
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Supply, Supplier, Stock, Material, Labour, LabourTypes, StockManagement, ConstructionSite, \
    LabourWorkTime, Client, Author, SiteManageger, CostEstimation, CementPrice, SteelPrice, BricksPrice, AggregatePrice, \
    SandPrice, FlooringPrice, PaintingPrice, SanitaryFittingsPrice, ElectricFittingPrice, LabourPrice, \
    SuppluStockUpdate, LabourRequest, Invoice


# Create your views here.



def supply_add(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')


def supply_list(request):
    if request.user.is_authenticated:
        obj = Supply.objects.all()[::-1]
        context={
            "obj":obj,
            "isact_supply": "active",
        }
        return render(request, "supply_management/supply_list.html", context)
    else:
        return redirect('login')


def supply_view(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Supply, id=id)
        context={
            "obj":obj,
            "isact_supply": "active",
        }
        return render(request, "supply_management/supply_view.html", context)
    else:
        return redirect('login')


def supply_update(request, id):
    if request.user.is_authenticated:
        supplier_obj = Supplier.objects.all()
        material = Material.objects.all()
        obj = get_object_or_404(Supply, id=id)
        context={
            "obj":obj,
            "supplier_obj":supplier_obj,
            "isact_supply": "active",
            "material":material
        }
        if request.method == "POST":
            supplier_company = request.POST.get("supplier_company_name")
            get_supplier = Supplier.objects.get(name=supplier_company)
            obj.supplier_company_name = get_supplier
            material_name = request.POST.get("material")
            get_material = Material.objects.get(material_name=material_name)
            obj.material = get_material
            obj.lot_no = request.POST.get("lot_no")
            obj.quantity = request.POST.get("quantity")
            obj.unit_price = request.POST.get("unit_price")
            obj.save()
            messages.success(request, "Supply Update Successfully")
            return redirect('list')
        return render(request, "supply_management/supply_update.html", context)
    else:
        return redirect('login')


def supply_remove(request, id):
    obj = get_object_or_404(Supply, id=id)
    obj.delete()
    messages.success(request, "Supply Delete Successfully")
    return redirect('list')


def supplier_list(request):
    if request.user.is_authenticated:
        sup_obj = Supplier.objects.all()[::-1]
        context={
            "sup_obj":sup_obj,
            'isact_supplier': 'active'
        }
        return render(request, "supply_management/supplier_list.html", context)
    else:
        return redirect('login')


def add_supplier(request):
    if request.user.is_authenticated:
        context={
            'isact_supplier': 'active'
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
    else:
        return redirect('login')


def update_supplier(request, id):
    if request.user.is_authenticated:
        supplier_obj = get_object_or_404(Supplier, id=id)
        context={
            "supplier":supplier_obj,
            'isact_supplier': 'active'
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
    else:
        return redirect('login')


def remove_supplier(request, id):
    obj = get_object_or_404(Supplier, id=id)
    obj.delete()
    messages.success(request, "Supplier Removed Successfully")
    return redirect('add_supplier')


def labour_type(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')


def update_labour_type(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(LabourTypes, id=id)
        if request.method == "POST":
            obj.labour_types = request.POST.get("labour_types")
            obj.save()
            messages.success(request, "Labour Type Update Successfully")
            return redirect('labour_type')
    else:
        return redirect('login')


def remove_labour_type(request, id):
    obj = get_object_or_404(LabourTypes, id=id)
    obj.delete()
    messages.success(request, "Labour Type Remove Successfully")
    return redirect('labour_type')


def labour_list(request):
    if request.user.is_authenticated:
        labour_obj = Labour.objects.all()[::-1]
        context={
            "labour": labour_obj,
            'isact_labourlist': 'active'
        }
        return render(request, "labour/labour_list.html", context)
    else:
        return redirect('login')


def add_new_labour(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')


def work_time_list(request):
    if request.user.is_authenticated:
        obj = LabourWorkTime.objects.all()
        context={
            "obj":obj,
            'isact_labourworktime': 'active'
        }
        return render(request, "labour/work_time_list.html", context)
    else:
        return redirect('login')


def remove_work_list(request, id):
    obj = get_object_or_404(LabourWorkTime, id=id)
    obj.delete()
    messages.success(request, "Work List Delete Successfully")
    return redirect('work_time_list')


def labour_request_list(request, filter):
    obj = None
    if filter == 'Approved':
        obj = LabourRequest.objects.all().filter(status=1)[::-1]
    elif filter == 'Pending':
        obj = LabourRequest.objects.all().filter(status=2)[::-1]
    elif filter == 'Rejected':
        obj = LabourRequest.objects.all().filter(status=3)[::-1]
    context = {
        "isact_labourrequestlist": "active",
        "obj": obj
    }
    return render(request,"labour_request/labour_request_list.html", context)


def add_labour_request(request):
    context={
        "isact_labourrequest":"active"
    }
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        labour_type = request.POST.get("labour_type")
        author= request.user
        name = ('Notification from site manager ' + '|' + 'please check the requirment,' + '|' + 'labour type :' + labour_type + '|' + 'Quantity:' + quantity)
        noti_obj = Notification(name=name)
        noti_obj.save()
        obj= LabourRequest(quantity=quantity,labour_type=labour_type)
        obj.save()
        messages.success(request, "Your Request Sent Successfully To Labour Manager")

    return render(request, "labour_request/add_labour_request.html", context)


def update_labour_request(request, id):
    obj = get_object_or_404(LabourRequest, id=id)
    context = {
        "isact_labourrequest": "active",
        "obj":obj
    }
    if request.method == "POST":
        obj.quantity = request.POST.get("quantity")
        obj.labour_type = request.POST.get("labour_type")
        obj.status = request.POST.get("status")
        obj.save()
        messages.success(request, "Update Successfully")
        return redirect('update_labour_request', id=id)
    return render(request,"labour_request/update_labour_request.html", context)

def remove_labour_request(request, id):
    obj = get_object_or_404(LabourRequest, id=id)
    obj.delete()
    messages.success(request, "Delete Successfully")
    return render(request,"labour_request")


def add_labour_work_time(request):
    if request.user.is_authenticated:
        cons_site = ConstructionSite.objects.all()
        lab = Labour.objects.all()
        context={
            "cons_site":cons_site,
            'isact_labourworktime':'active',
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
    else:
        return redirect('login')


def update_labour_work_time(request, id):
    if request.user.is_authenticated:
        cons_site = ConstructionSite.objects.all()
        lab = Labour.objects.all()
        labour_work_time = get_object_or_404(LabourWorkTime, id=id)
        context={
            "cons_site":cons_site,
            'isact_labourworktime':'active',
            "lab":lab,
            "labour_work_time":labour_work_time
        }
        if request.method == "POST":
            consturction_site_obj = request.POST.get("consturction_site")
            labour_work_time.consturction_site = ConstructionSite.objects.get(location=consturction_site_obj)
            labour_obj = request.POST.get("labour")
            labour_work_time.labour = Labour.objects.get(name=labour_obj)
            labour_work_time.start_date = request.POST.get("start_date")
            labour_work_time.end_date = request.POST.get("end_date")
            labour_work_time.save()
            messages.success(request, "Labour Work Time Added Successfully")
            return redirect("work_time_list")
        return render(request, "labour/update_labour_work_time.html", context)
    else:
        return redirect('login')


def labour_update(request, id):
    if request.user.is_authenticated:
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
                obj.photo = request.FILES.get("photo")
            obj.save()
            messages.success(request, "Labour Update Successfully!!")
            return redirect('labour_list')
        return render(request, "labour/update_labour.html", context)
    else:
        return redirect('login')

def remove_labour(request, id):
    obj = get_object_or_404(Labour, id=id)
    obj.delete()
    messages.success(request, "Labour removed successfully")
    return redirect('labour_list')


def remove_stock(request, id):
    obj = get_object_or_404(Stock, id=id)
    obj.delete()
    messages.success(request, "Stock Removed Successfully")
    return redirect('stock_list')


def add_new_stock(request):
    if request.user.is_authenticated:
        obj = Material.objects.all()
        context={
            "obj":obj,
             'isact_stocklist': 'active',
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
    else:
        return redirect('login')


def update_stock(request, id):
    if request.user.is_authenticated:
        mate = Material.objects.all()
        obj = get_object_or_404(Stock, id=id)
        context={
            "obj":obj,
            "mate":mate,
            'isact_stocklist': 'active'

        }
        if request.method == "POST":
            material_obj = request.POST.get("material")
            obj.material = Material.objects.get(material_name=material_obj)
            obj.name = request.POST.get("name")
            obj.quantity = request.POST.get("quantity")
            obj.save()
            messages.success(request, "Stock Update Successfully")
            return redirect('stock_list')
        return render(request, "stock/update_stock.html", context)
    else:
        return redirect('login')


def stock_management(request):
    if request.user.is_authenticated:
        obj = SiteManageger.objects.all().filter(is_approve=1)[::-1]
        context={
            "obj":obj,
            'isact_stockmanagement': 'active',

        }
        return render(request, "stock/stock_management.html", context)
    else:
        return redirect('login')


def remove_stock_management(request, id):
    obj = get_object_or_404(StockManagement, id=id)
    obj.delete()
    messages.success(request, "Stock management Deleted Successfully")
    return redirect('stock_management')


def add_stock_management(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')


def update_stock_management(request, id):
    if request.user.is_authenticated:
        obj = ConstructionSite.objects.all()
        material_obj = Material.objects.all()
        get_stock_management = get_object_or_404(StockManagement, id=id)
        if request.method == "POST":
            construct_site_obj = request.POST.get("construct_site")
            get_stock_management.construct_site = ConstructionSite.objects.get(location=construct_site_obj)
            mat_obj = request.POST.get("material")
            get_stock_management.material = Material.objects.get(material_name=mat_obj)
            get_stock_management.quantity = request.POST.get("quantity")
            get_stock_management.save()
            messages.success(request, "Update Successfully")
            return redirect('stock_management')
        context={
            "isact_stockmanagement": "active",
            "material_obj":material_obj,
            "get_stock_management":get_stock_management,
            "obj":obj
        }
        return render(request, "stock/update_stock_management.html", context)
    else:
        return redirect('login')


def client_list(request):
    if request.user.is_authenticated:
        client_obj = Client.objects.all()[::-1]
        context={
            "isact_clientlist":"active",
            "client":client_obj
        }
        return render(request, "client/client_list.html", context)
    else:
        return redirect('login')


def add_new_client(request):
    if request.user.is_authenticated:
        context={
            "isact_clientlist":"active",
        }
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            address = request.POST.get("address")
            emergency_contact = request.POST.get("emergency_contact")
            date_of_birth = request.POST.get("date_of_birth")
            nid_number = request.POST.get("nid_number")
            photo = request.FILES.get("photo")
            obj = Client(name=name,phone=phone,email=email,address=address,emergency_contact=emergency_contact,date_of_birth=date_of_birth,nid_number=nid_number,photo=photo)
            obj.save()
            messages.success(request, "New Client Added Successfully")
            return redirect('client_list')
        return render(request, "client/add_new_client.html",context)
    else:
        return redirect('login')


def update_client(request, id):
    if request.user.is_authenticated:
        client = get_object_or_404(Client, id=id)
        context={
            "isact_clientlist":"active",
            "client":client
        }
        if request.method == "POST":
            client.name = request.POST.get("name")
            client.phone = request.POST.get("phone")
            client.email = request.POST.get("email")
            client.address = request.POST.get("address")
            client.emergency_contact = request.POST.get("emergency_contact")
            client.date_of_birth = request.POST.get("date_of_birth")
            client.nid_number = request.POST.get("nid_number")
            client.photo = request.FILES.get("photo")
            client.save()
            messages.success(request, "Client Updated Successfully")
            return redirect('client_list')
        return render(request, "client/update_client.html",context)
    else:
        return redirect('login')


def remove_client(request, id):
    obj = get_object_or_404(Client, id=id)
    obj.delete()
    messages.success(request, "Client remove Successfully")
    return redirect('client_list')


def estimate(request):
    cons_obj=ConstructionSite.objects.all()
    if request.user.is_authenticated:
        obj = CostEstimation.objects.last()
        if obj == None:
            obj=0

        context = {
            'cons_obj':cons_obj,
            'obj': obj,
            'isact_costestimation': 'active'
        }

        if request.method == "POST":
            constrcution_site_obj = request.POST.get("constrcution_site")
            constrcution_site =ConstructionSite.objects.get(id=constrcution_site_obj)
            area = request.POST.get("area")
            obj = CostEstimation(area=area, constrcution_site=constrcution_site)
            obj.save()
            messages.success(request, "see the total calculate")
            return redirect('estimate')
        return render(request, "cost_estimation/estimate_page.html", context)
    else:
        return redirect('login')

def cost_estimation_details(request, id):
    get_cement = CementPrice.objects.last()
    cement_price = get_cement.price

    get_steel = SteelPrice.objects.last()
    steel_price = get_steel.price

    get_bricks = BricksPrice.objects.last()
    bricks_price = get_bricks.price

    get_sand = SandPrice.objects.last()
    sand_price = get_sand.price

    get_aggregate = AggregatePrice.objects.last()
    aggregate_price = get_aggregate.price


    get_flooring = FlooringPrice.objects.last()
    flooring_price = get_flooring.price

    get_painting = PaintingPrice.objects.last()
    painting_price = get_painting.price

    get_sanitary_fittings = SanitaryFittingsPrice.objects.last()
    sanitary_fittings_price = get_sanitary_fittings.price

    get_electric_fitting = ElectricFittingPrice.objects.last()
    electric_fitting_price = get_electric_fitting.price

    get_labour = LabourPrice.objects.last()
    labourting_price = get_labour.price

    if request.user.is_authenticated:
        obj = get_object_or_404(CostEstimation, id=id)
        area_obj = obj.area

        labour_per_day= 11 / 100
        required_labour = int(labour_per_day * area_obj)
        total_labour_price = int(labourting_price * required_labour)

        cement_per_square =45/100
        required_cement = int(cement_per_square*area_obj)
        total_cement_price = int(cement_price * required_cement)

        stell_per_square = 350 / 100
        required_steel = int(stell_per_square * area_obj)
        total_steel_price = int(steel_price * required_steel)

        bricks_per_square = 2000/ 100
        required_bricks = int(bricks_per_square * area_obj)
        total_bricks_price = int(bricks_price * required_bricks)

        steel_per_sand = 195 / 100
        required_sand = int(steel_per_sand * area_obj)
        total_sand_price = int(sand_price * required_sand)

        steel_per_aggregate = 210 / 100
        required_aggregate = int(steel_per_aggregate * area_obj)
        total_aggregate_price = int(aggregate_price * required_aggregate)

        steel_per_flooring = 105 / 100
        required_flooring = int(steel_per_flooring * area_obj)
        total_flooring_price = int(flooring_price * required_flooring)

        steel_per_painting = 600 / 100
        required_painting = int(steel_per_painting * area_obj)
        total_painting_price = int(painting_price * required_painting)

        steel_per_sanitary_fittings = 150 / 100
        required_sanitary_fittings = int(steel_per_sanitary_fittings * area_obj)
        total_sanitary_fittings_price = int(sanitary_fittings_price * required_sanitary_fittings)

        steel_per_electric_fitting = 15 / 100
        required_electric_fitting = int(steel_per_electric_fitting * area_obj)
        total_electric_fitting_price = int(electric_fitting_price * required_electric_fitting)
        total_price = int(total_cement_price + total_steel_price + total_bricks_price + total_sand_price + total_aggregate_price + total_flooring_price + total_painting_price + total_sanitary_fittings_price + total_electric_fitting_price)

        context={
            'obj':obj,
            'required_labour':required_labour,
            'total_labour_price':total_labour_price,

            'isact_costestimation':'active',
            "cemet_price":get_cement,
            "required_cement": required_cement,
            "total_cement_price": total_cement_price,
            "total_price":total_price,
            "steel_price":steel_price,
            "required_steel":required_steel,
            "total_steel_price": total_steel_price,
            "bricks_price":bricks_price,
            "required_bricks":required_bricks,
            "total_bricks_price":total_bricks_price,
            "sand_price":sand_price,
            "required_sand": required_sand,
            "total_sand_price": total_sand_price,
            "aggregate_price":aggregate_price,
            "required_aggregate":required_aggregate,
            "total_aggregate_price":total_aggregate_price,
            "flooring_price":flooring_price,
            "required_flooring":required_flooring,
            "total_flooring_price":total_flooring_price,
            "painting_price":painting_price,
            "required_painting":required_painting,
            "total_painting_price":total_painting_price,
            "sanitary_fittings_price":sanitary_fittings_price,
            "required_sanitary_fittings":required_sanitary_fittings,
            "total_sanitary_fittings_price":total_sanitary_fittings_price,
            "electric_fitting_price":electric_fitting_price,
            "required_electric_fitting":required_electric_fitting,
            "total_electric_fitting_price":total_electric_fitting_price

        }
        return render(request, "cost_estimation/cost_estimation_pdf.html", context)
    else:
        return redirect('login')


def cost_estimation_pdf_view(request):

    template_path = 'cost_estimation/cost_pdf_view.html'
    #obj = obj query
    context = {    }
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def register_surveyor(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST.get('fname', )
            lname = request.POST.get('lname', )
            uname = request.POST.get('uname', )
            password = request.POST.get('password', )
            address = request.POST.get("address")
            profile_picture = request.FILES.get("profile_picture")
            country = request.POST.get("country")
            division = request.POST.get("division")
            district = request.POST.get("district")
            sub_district = request.POST.get("sub_district")
            email = request.POST.get("email")
            area = request.POST.get("area")
            phone = request.POST.get("phone")
            designation = request.POST.get("designation")
            experience = request.POST.get("experience")
            description = request.POST.get("description")
            graduation_subject = request.POST.get("graduation_subject")
            university = request.POST.get("university")
            user = User.objects.all().filter(username=uname)
            if user :
                messages.success(request, "User Already Exits")
                return redirect('register_surveyor')
            else :
                auth_info={
                    'first_name': fname,
                    'last_name': lname,
                    'username': uname,
                    'password': make_password(password),
                }
                user = User(**auth_info)
                user.save()
            user_obj = Author(experience=experience,university=university,description=description,graduation_subject=graduation_subject,user=user,address=address,profile_picture=profile_picture,country=country,division=division,
                                district=district,sub_district=sub_district,email=email,area=area,
                                phone=phone,designation=designation)
            user_obj.save()
            messages.success(request, "User Create Successfully !!")
        context = {
            "isact_registersurveyor": "active"
        }
        return render(request, "surveyor/register_surveyor.html", context)
    else:
        return redirect('login')


def update_surveyor(request, id):
    if request.user.is_authenticated:
        user_obj = get_object_or_404(Author, id=id)
        if request.method == "POST":
            user_obj.address = request.POST.get("address")
            user_obj.profile_picture = request.POST.get("profile_picture")
            user_obj.country = request.POST.get("country")
            user_obj.division = request.POST.get("division")
            user_obj.district = request.POST.get("district")
            user_obj.sub_district = request.POST.get("sub_district")
            user_obj.email = request.POST.get("email")
            user_obj.graduation_subject = request.POST.get("graduation_subject")
            user_obj.university = request.POST.get("university")
            user_obj.Skills = request.POST.get("Skills")
            user_obj.area = request.POST.get("area")
            user_obj.phone = request.POST.get("phone")
            user_obj.description = request.POST.get("description")
            user_obj.designation = request.POST.get("designation")
            user_obj.experience = request.POST.get("experience")
            user_obj.role = request.POST.get("role")
            user_obj.status = request.POST.get("status")
            user_obj.save()
            messages.success(request, "User Update Successfully !!")
            return redirect('update_surveyor', id=id)

        context ={
            "user": user_obj,
            "isact_surveyorlist": "active",
        }
        return render(request, "surveyor/surveyor_update.html", context)
    else:
        return redirect('login')

@login_required
def remove_surveyor(request, id):
    obj = get_object_or_404(User, id=id)
    obj.delete()
    messages.success(request, "Requested User Delete Successfully !!")
    return redirect('surveyor_list', 'None')


def surveyor_list(request, filter):
    if request.user.is_authenticated:
        user_obj = None
        if filter == 'None':
            user_obj = Author.objects.all()[::-1]
        elif filter == 'active':
            user_obj = Author.objects.all().filter(status=1)[::-1]
        elif filter == 'inactive':
            user_obj = Author.objects.all().filter(status=2)[::-1]
        elif filter == 'rejected':
            user_obj = Author.objects.all().filter(status=3)[::-1]

        context ={
            "isact_surveyorlist": "active",
            "user": user_obj
        }
        return render(request, "surveyor/surveyor_list.html", context)
    else:
        return redirect('login')


def view_surveyor(request, id):
    if request.user.is_authenticated:
        user_obj = Author.objects.get(id=id)

        context= {
            "user": user_obj,
            "isact_surveyorlist": "active",
        }
        return render(request, "surveyor/view_surveyor.html", context)
    else:
        return redirect('login')


def stock_list(request):
    if request.user.is_authenticated:
        obj = Stock.objects.all()[::-1]
        stock_obj = Stock.objects.all()
        total_quantity = stock_obj.aggregate(Sum('quantity'))['quantity__sum']
        site_obj = SiteManageger.objects.filter(is_approve=1)
        total_quantity_site = site_obj.aggregate(Sum('quantity'))['quantity__sum']
        if total_quantity_site is None:
            total_quantity_site = 0
        if total_quantity is None:
            total_quantity = 0
        total =total_quantity - total_quantity_site

        context={
            "obj":obj,
            "total":total,
            "total_quantity":int(total_quantity),
            "total_quantity_site":total_quantity_site,
            "isact_stocklist": "active",
        }
        return render(request, "stock/stock_list.html", context)
    else:
        return redirect('login')


def site_manager_request_list(request, filter):
    if request.user.is_authenticated:
        obj = None
        if filter == 'Pending':
            obj = SiteManageger.objects.all().filter(is_approve=2)[::-1]
        elif filter == 'Approved':
            obj = SiteManageger.objects.all().filter(is_approve=1)[::-1]
        elif filter == 'Rejected':
            obj = SiteManageger.objects.all().filter(is_approve=3)[::-1]

        site_obj = SiteManageger.objects.filter(is_approve=True)
        total_quantity = site_obj.aggregate(Sum('quantity'))['quantity__sum']
        context = {
            "obj":obj,
            'total_required_quantity': total_quantity,
            "isact_sitemanager": "active",
        }
        return render(request, "stock/site_manager_request_list.html", context)
    else:
        return redirect('login')


def site_manager_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            category = request.POST.get("category")
            material = request.POST.get("material")
            quantity = request.POST.get("quantity")
            manager_obj = SiteManageger(category=category, material=material, quantity=quantity, site_manager=request.user)
            manager_obj.save()
            messages.success(request, "Your Request Send to our Admin, Please Wait for his approval")
            return redirect('site_manager_request_list', filter='Pending')
        context={
            "isact_site_manager": "active",
        }
        return render(request, "stock/site_manager_request.html", context)
    else:
        return redirect('login')


def site_manager_update(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(SiteManageger, id=id)
        context={
            "obj":obj
        }
        if request.method == "POST":
            obj.is_approve = request.POST.get("is_approve")
            obj.save()
            messages.success(request, "Site Manager Request Update Successfully ")
            return redirect('site_manager_request_list', filter='Pending')
        return render(request, "stock/site_manageger_request_update.html", context)
    else:
        return redirect('login')


def site_manager_request_delete(request, id):
    obj = get_object_or_404(SiteManageger, id=id)
    obj.delete()
    messages.success(request, "Successfully Remove")
    return redirect('site_manager_request_list', filter='Pending')


def material(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            material_name = request.POST.get("material_name")
            type = request.POST.get("type")
            mat_obj = Material(material_name = material_name,type =type)
            mat_obj.save()
            messages.success(request, "Country Added Successfully")
        get_material = Material.objects.all()[::-1]
        context = {
            "get_material": get_material,
            'isact_material': 'active',
        }
        return render(request, "add/add_material.html", context)
    else:
        return redirect('login')

@login_required
def material_remove(request, id):
    obj = get_object_or_404(Material, id=id)
    obj.delete()
    messages.success(request, "Material Remove Successfully")
    return redirect('material_list')


def cement_price(request):
    get_price = CementPrice.objects.last()
    if request.method =="POST":
        price = request.POST.get("price")
        obj = CementPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('cement_price')
    context={
        'isact_price':'active',
        'price':get_price
    }
    return render(request, "price/add/add_cement_price.html",context)

def steel_price(request):
    get_price = SteelPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = SteelPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('steel_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/add_steel_price.html",context)

def aggregate_price(request):
    get_price = AggregatePrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = AggregatePrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('aggregate_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/aggregate_price.html",context)

def bricks_price(request):
    get_price = BricksPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = BricksPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('bricks_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/bricks_price.html",context)

def electric_fitting_price(request):
    get_price = ElectricFittingPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = ElectricFittingPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('electric_fitting_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/electric_fitting_price.html",context)

def flooring_price(request):
    get_price = FlooringPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = FlooringPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('flooring_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/flooring_price.html",context)

def painting_price(request):
    get_price = PaintingPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = PaintingPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('painting_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/painting_price.html",context)

def sand_price(request):
    get_price = SandPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = SandPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('sand_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/sand_price.html",context)

def sanitary_price(request):
    get_price = SanitaryFittingsPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = SanitaryFittingsPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('sanitary_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/sanitary_price.html",context)


def add_labour_price(request):
    get_price = LabourPrice.objects.last()
    if request.method == "POST":
        price = request.POST.get("price")
        obj = LabourPrice(price=price)
        obj.save()
        messages.success(request, "Price Update Successfully")
        return redirect('add_labour_price')
    context = {
        'isact_price': 'active',
        'price': get_price
    }
    return render(request, "price/add/add_labour_price.html", context)


def construction_site_list(request):
    obj = ConstructionSite.objects.all()
    context={
        "obj":obj,
        "isact_constructionsite":"active"
    }
    return render(request, "construction_site/site_manager_list.html", context)

def add_new_construction_site(request):
    get_client = Client.objects.all()
    context={
        "get_client":get_client
    }
    if request.method == "POST":
        client_obj = request.POST.get("client")
        client = Client.objects.get(id=client_obj)
        location = request.POST.get("location")
        landarea = request.POST.get("landarea")
        rajuk_no = request.POST.get("rajuk_no")
        architect_name = request.POST.get("architect_name")
        architect_reg_no = request.POST.get("architect_reg_no")
        starting_date = request.POST.get("starting_date")
        end_date = request.POST.get("end_date")
        obj = ConstructionSite(client=client, location=location, landarea=landarea, rajuk_no=rajuk_no,
                               architect_name=architect_name, architect_reg_no=architect_reg_no,
                               starting_date=starting_date, end_date=end_date)
        obj.save()
        messages.success(request, "New Site Added Successfully")
        return redirect('construction_list')
    return render(request, "construction_site/add_new_construction_site.html", context)


def update_construction_site(request, id):
    get_client = Client.objects.all()
    obj= get_object_or_404(ConstructionSite, id=id)
    context={
        "obj":obj,
        "get_client":get_client
    }
    if request.method == "POST":
        client_obj = request.POST.get("client")
        obj.client = Client.objects.get(id=client_obj)
        obj.location = request.POST.get("location")
        obj.landarea = request.POST.get("landarea")
        obj.rajuk_no = request.POST.get("rajuk_no")
        obj.architect_name = request.POST.get("architect_name")
        obj.architect_reg_no = request.POST.get("architect_reg_no")
        obj.starting_date = request.POST.get("starting_date")
        obj.end_date = request.POST.get("end_date")
        obj.save()
        messages.success(request, "Construction Site Update Successfully")
        return redirect('construction_list')
    return render(request, "construction_site/update_construction.html", context)



def remove_contruction_site(request, id):
    obj= get_object_or_404(ConstructionSite, id=id)
    obj.delete()
    messages.success(request, "Delete Successfully")
    return redirect('construction_list')


def stock_manager_request_list(request, filter):
    obj = None
    if filter == 'Approved':
        obj = SuppluStockUpdate.objects.all().filter(is_approve=1)[::-1]
    elif filter == 'Pending':
        obj = SuppluStockUpdate.objects.all().filter(is_approve=2)[::-1]
    elif filter == 'Rejected':
        obj = SuppluStockUpdate.objects.all().filter(is_approve=3)[::-1]
    context = {
        "isact_requestlist": "active",
        "obj": obj
    }
    return render(request, "stock/stock_manager_request_list.html", context)


def stock_request_to_supplier(request):
    if request.method == "POST":
        stock_manager_name = request.POST.get("stock_manager_name")
        material_type = request.POST.get("material_type")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")

        name = ('Notification from '+stock_manager_name+ '|'+'Stock is Running Out,please check the requirment,'+'|'+'material type :'+material_type+'|'+'Quantity:'+quantity+'|'+'Update Message :'+description)
        noti_obj = Notification(name=name)
        noti_obj.save()
        obj = SuppluStockUpdate(stock_manager_name=stock_manager_name,material_type=material_type,quantity=quantity,description=description)
        obj.save()
        messages.success(request, "Your request Sent to The Supplier Manager, please Wait For Response")
    return render(request, "stock/stock_request_supplier.html")


def stock_manager_request_list_update(request, id):
    obj = get_object_or_404(SuppluStockUpdate, id=id)
    context={
        "obj":obj
    }
    if request.method == "POST":
        obj.stock_manager_name = request.POST.get("stock_manager_name")
        obj.material_type = request.POST.get("material_type")
        obj.quantity = request.POST.get("quantity")
        obj.description = request.POST.get("description")
        obj.is_approve = request.POST.get("is_approve")
        obj.save()
        messages.success(request, "Update Successfully")
        return redirect("stock_manager_request_list_update", id=id)
    return render(request, "stock/stock_manager_request_list_update.html", context)


def stock_manager_request_list_remove(request, id):
    obj = get_object_or_404(SuppluStockUpdate, id=id)
    obj.delete()
    messages.success(request, "Delete Successfully")
    return redirect("stock_manager_request_list", filter="Pending")


def notification_list(request):
    noti_obj = Notification.objects.all()[::-1]
    stock_obj = Stock.objects.all()
    total_quantity = stock_obj.aggregate(Sum('quantity'))['quantity__sum']
    site_obj = SiteManageger.objects.filter(is_approve=1)
    total_quantity_site = site_obj.aggregate(Sum('quantity'))['quantity__sum']
    if total_quantity_site is None:
        total_quantity_site = 0
    if total_quantity is None:
        total_quantity = 0
    total = total_quantity - total_quantity_site

    context={
        "total":total,
        "notification":noti_obj,
        "isact_notification":"active"
    }
    return render(request, "notification/notification_list.html", context)

def remove_notification(request,id):
    obj = get_object_or_404(Notification, id=id)
    obj.delete()
    messages.success(request, "Notification remove Successfully")
    return redirect('notification_list')


def invoice_list(request):
    obj = Invoice.objects.all()[::-1]
    context={
        "obj":obj
    }
    return render(request, "invoice/invoice_list.html",context)


def add_new_invoice(request):
    sup_obj =Supplier.objects.all()
    context={
        "sup_obj":sup_obj
    }
    if request.method == "POST":
        supply_details_obj = request.POST.get("supply_details")
        print(supply_details_obj)
        supply_details = Supply.objects.get(id=supply_details_obj)
        payment = request.POST.get("payment")
        due = request.POST.get("due")
        obj = Invoice(supply_details=supply_details,payment=payment,due=due)
        obj.save()
        messages.success(request, "Invoice Add Successfully")
        return redirect('invoice_list')
    return render(request, "invoice/add_new_invoice.html", context)


def invoice_details(request, id):
    obj = get_object_or_404(Invoice, id=id)
    context={
        "obj":obj
    }
    return render(request, "invoice/invoice_details.html", context)

def invoice_remove(request, id):
    obj = get_object_or_404(Invoice, id=id)
    obj.delete()
    messages.success(request, "Delete Successfully")
    return redirect('invoice_list')
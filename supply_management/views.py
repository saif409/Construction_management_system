from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.base import View
# for Pdf views
# for pff import 
from io import BytesIO
from django.views import View
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Supply, Supplier, Stock, Material, Labour, LabourTypes, StockManagement, ConstructionSite, \
    LabourWorkTime, Client, Author


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
        "obj":obj,
        'isact_labourworktime': 'active'
    }
    return render(request, "labour/work_time_list.html", context)

def remove_work_list(request, id):
    obj = get_object_or_404(LabourWorkTime, id=id)
    obj.delete()
    messages.success(request, "Work List Delete Successfully")
    return redirect('work_time_list')


def add_labour_work_time(request):
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


def update_labour_work_time(request, id):
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
            obj.photo = request.FILES.get("photo")
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
        'isact_stocklist': 'active',
        "total_quantity":total_quantity
    }
    return render(request, "stock/stock_list.html",context)

def remove_stock(request, id):
    obj = get_object_or_404(Stock, id=id)
    obj.delete()
    messages.success(request, "Stock Removed Successfully")
    return redirect('stock_list')

def add_new_stock(request):
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


def update_stock(request, id):
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


def stock_management(request):
    obj = StockManagement.objects.all()
    context={
        "obj":obj,
        'isact_stockmanagement': 'active',

    }
    return render(request, "stock/stock_management.html", context)

def remove_stock_management(request, id):
    obj = get_object_or_404(StockManagement, id=id)
    obj.delete()
    messages.success(request, "Stock management Deleted Successfully")
    return redirect('stock_management')


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


def update_stock_management(request, id):
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


def client_list(request):
    client_obj = Client.objects.all()[::-1]
    context={
        "isact_clientlist":"active",
        "client":client_obj
    }
    return render(request, "client/client_list.html", context)


def add_new_client(request):
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


def update_client(request, id):
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


def remove_client(request, id):
    obj = get_object_or_404(Client, id=id)
    obj.delete()
    messages.success(request, "Client remove Successfully")
    return redirect('client_list')


def cost_estimation_details(request):
    area = 100
    one_bag_cement = (100/45)
    cal_cement = one_bag_cement * area

    print(cal_cement)
    context={
        'isact_costestimation':'active'
    }
    return render(request, "cost_estimation/cost_estimation_pdf.html", context)

# pdf file added 
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

# for downloading pdf 
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class cost_estimation_pdf_download(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('cost_estimation/cost_pdf_view.html')

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = 'Invoice_%s.pdf' %("12341231")
		content = "attachment; filename= %s" %(filename)
		response['Content-Disposition'] = content
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
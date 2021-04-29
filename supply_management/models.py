from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class LabourTypes(models.Model):
    labour_types = models.CharField(max_length=200)

    def __str__(self):
        return self.labour_types


class Labour(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    labour_type = models.ForeignKey(LabourTypes, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200)
    nid_number = models.CharField(max_length=200)
    photo = models.ImageField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    comments = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    material_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.material_name


class Supply(models.Model):
    supplier_company_name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    lot_no = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    unit_price = models.IntegerField(null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.supplier_company_name.name


class Stock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    update_date = models.DateField(auto_now=True)
    update_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RequestStock(models.Model):
    material =  models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    nid_number = models.CharField(max_length=200)
    photo = models.FileField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ConstructionSite(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    landarea = models.CharField(max_length=200)
    rajuk_no = models.CharField(max_length=200)
    architect_name = models.CharField(max_length=200)
    architect_reg_no = models.CharField(max_length=200)
    starting_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return self.location


class LabourWorkTime(models.Model):
    consturction_site = models.ForeignKey(ConstructionSite, on_delete=models.CASCADE)
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return self.labour.name


class StockManagement(models.Model):
    construct_site = models.ForeignKey(ConstructionSite, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


class Invoice(models.Model):
    supply_details = models.ForeignKey(Supply, on_delete=models.CASCADE)
    payment = models.CharField(max_length=200)
    due = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.payment


ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Supplier Manager'),
    (3, 'Stock Manager'),
    (4, 'Site Manager'),
    (5, 'Labour Manager'),
)

STATUS_CHOICES = (
    (1, 'Active'),
    (2, 'InActive'),
    (3, 'Rejected'),
)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField(null=True, blank=True)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sub_district = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    graduation_subject = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = models.TextField()
    designation = models.CharField(max_length=100)
    experience = models.CharField(max_length=200)
    role = models.IntegerField(choices=ROLE_CHOICES, null=True, default=3)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, default=2)

    def __str__(self):
        return str(self.user)


STATUS_CHOICES_SiteManageder = (
    (1, 'Approved'),
    (2, 'Pending'),
    (3, 'Rejected'),
)


class SiteManageger(models.Model):
    category = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    quantity = models.IntegerField()
    site_manager = models.CharField(max_length=200)
    is_approve = models.IntegerField(choices=STATUS_CHOICES_SiteManageder, default=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category


class CostEstimation(models.Model):
    constrcution_site = models.ForeignKey(ConstructionSite, models.CASCADE)
    area = models.IntegerField(default=0)




class CementPrice(models.Model):
    price = models.IntegerField(default=0)


class SteelPrice(models.Model):
    price = models.IntegerField(default=0)


class BricksPrice(models.Model):
    price = models.IntegerField(default=0)


class AggregatePrice(models.Model):
    price = models.IntegerField(default=0)

class SandPrice(models.Model):
    price = models.IntegerField(default=0)

class FlooringPrice(models.Model):
    price = models.IntegerField(default=0)

class PaintingPrice(models.Model):
    price = models.IntegerField(default=0)

class SanitaryFittingsPrice(models.Model):
    price = models.IntegerField(default=0)


class ElectricFittingPrice(models.Model):
    price = models.IntegerField(default=0)

class LabourPrice(models.Model):
    price = models.IntegerField(default=0)


REQUEST_CHOICES = (
    (1, 'Approved'),
    (2, 'Pending'),
    (3, 'Rejected'),
)


class SuppluStockUpdate(models.Model):
    stock_manager_name = models.CharField(max_length=200)
    material_type = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    description = models.TextField()
    is_approve = models.IntegerField(choices=REQUEST_CHOICES, default=2)

    def __str__(self):
        return self.material_type

class LabourRequest(models.Model):
    quantity = models.CharField(max_length=200)
    labour_type = models.CharField(max_length=200)
    status = models.IntegerField(choices=REQUEST_CHOICES, default=2)

    def __str__(self):
        return self.quantity
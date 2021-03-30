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
    quantity = models.CharField(max_length = 200)
    update_date = models.DateField(auto_now=True)
    update_by = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    nid_number = models.CharField(max_length=200)
    photo = models.FileField()

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
    date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.labour.name

class StockManagement(models.Model):
    construct_site = models.ForeignKey(ConstructionSite, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
    date = models.DateField()


class Invoice(models.Model):
    supply_details = models.ForeignKey(Supply, on_delete=models.CASCADE)
    payment = models.CharField(max_length=200)
    due = models.CharField(max_length=200)

    def __str__(self):
        return self.payment



from django.db import models

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_adminregistration(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district, on_delete=models.CASCADE)
class tbl_subcategory(models.Model):
    subcat_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)    
class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=50)   
class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_gender=models.CharField(max_length=50)
    employee_contact=models.CharField(max_length=50)
    employee_dob=models.CharField(max_length=50)
    employee_salary=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department, on_delete=models.CASCADE)
    designation=models.ForeignKey(tbl_designation, on_delete=models.CASCADE)
class tbl_ward(models.Model):
    ward_number=models.CharField(max_length=50)
class tbl_wastecategory(models.Model):
    wastecategory_name=models.CharField(max_length=50)




from django.db import models
from Admin.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contactno=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)  
    user_houseno=models.CharField(max_length=50)  
    user_photo=models.FileField(upload_to='Assets/UserDocs/')
    ward_id=models.ForeignKey(tbl_ward,on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)
class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_contactno=models.CharField(max_length=50)
    seller_email=models.CharField(max_length=50)
    seller_password=models.CharField(max_length=50)
    seller_establishdate=models.CharField(max_length=50)  
    seller_Licenseno=models.CharField(max_length=50) 
    seller_ownername=models.CharField(max_length=50)  
    seller_licenseproof=models.FileField(upload_to='Assets/SellerDocs/')
    seller_idproof=models.FileField(upload_to='Assets/SellerDocs/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    seller_status=models.IntegerField(default=0)
class tbl_worker(models.Model):
    worker_name=models.CharField(max_length=50)
    worker_email=models.CharField(max_length=50)
    worker_contact=models.CharField(max_length=50)
    worker_address=models.CharField(max_length=50)
    worker_photo=models.FileField(upload_to='Assets/workerDocs/')
    worker_password=models.CharField(max_length=50)
    worker_proof=models.FileField(upload_to='Assets/workerDocs/')
    worker_status=models.IntegerField(default=0)
    worker_latitude=models.CharField(max_length=50,null=True)
    worker_longitude=models.CharField(max_length=50,null=True)
    worker_curr_city=models.CharField(max_length=50,null=True)
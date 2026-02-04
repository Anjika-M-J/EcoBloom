from django.db import models
from Guest.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
class tbl_waste(models.Model):
    waste_date=models.DateField(auto_now_add=True)
    waste_qty=models.IntegerField(default=0)
    wastecategory_id=models.ForeignKey(tbl_wastecategory, on_delete=models.CASCADE)
    waste_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
class tbl_payment(models.Model):
    payment_amount=models.IntegerField(default=50)
    payment_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    payment_status=models.IntegerField(default=0)
    

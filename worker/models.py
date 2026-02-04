from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.
class tbl_assignward(models.Model):
    assignward_date=models.DateField(auto_now_add=True)
    ward_id=models.ForeignKey(tbl_ward, on_delete=models.CASCADE)
    worker_id=models.ForeignKey(tbl_worker, on_delete=models.CASCADE)
class tbl_workerattendence(models.Model):
    workerattendence_datetime=models.DateField(auto_now_add=True)
    workerattendence_status=models.IntegerField(default=0)
    worker_id=models.ForeignKey(tbl_worker, on_delete=models.CASCADE)
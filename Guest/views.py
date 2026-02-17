from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from worker.models import *
# Create your views here.


def NewUser(request):
    warddata=tbl_ward.objects.all()
    if request.method=="POST":
        username=request.POST.get("txt_name")
        userhouseno=request.POST.get("txt_hno")
        usercontact=request.POST.get("txt_con")
        useremail=request.POST.get("txt_email")
        userpassword=request.POST.get("txt_pass")
        userconfpassword=request.POST.get("txt_confpass")
        useraddress=request.POST.get("txt_address")
        userphoto=request.FILES.get("txt_photo")
        ward=tbl_ward.objects.get(id=request.POST.get("sel_ward"))  
        newusercount=tbl_user.objects.filter(user_houseno=userhouseno).count()
        if newusercount>0:
            return render(request,"Guest/NewUser.html",{'msg':"User Already exist"})
        else:
            tbl_user.objects.create(user_name=username,user_houseno=userhouseno,user_contactno=usercontact,user_email=useremail,user_password=userpassword,user_address=useraddress,user_photo=userphoto,ward_id=ward)  
        return render(request,"Guest/NewUser.html",{'msg':"Registration Successfull"})
    else:
        return render(request,"Guest/NewUser.html",{'warddata':warddata})

def AjaxPlace(request):
    districtid=request.GET.get('did')
    placedata=tbl_place.objects.filter(district=districtid)
    return render(request,"Guest/AjaxPlace.html",{'placedata':placedata})
def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_adminregistration.objects.filter(admin_email=email,admin_password=password).count()
        sellercount=tbl_seller.objects.filter(seller_email=email,seller_password=password).count()
        workercount=tbl_worker.objects.filter(worker_email=email,worker_password=password).count()
        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect("User:HomePage")
        elif admincount>0:
            admindata=tbl_adminregistration.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect("Admin:HomePage")
        elif sellercount>0:
            sellerdata=tbl_seller.objects.get(seller_email=email,seller_password=password)
            request.session['sid']=sellerdata.id
            return redirect("Seller:SellerHomePage")
        elif workercount>0:
            workerdata=tbl_worker.objects.get(worker_email=email,worker_password=password)
            if workerdata.worker_status==1:
                request.session['wid']=workerdata.id
                return redirect("worker:WorkerHomePage")
            elif workerdata.worker_status==2:
                return render(request,"Guest/Login.html",{'msg':"Rejected"})
            else:
                return render(request,"Guest/Login.html",{'msg':"Pending"})
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid Login"})
    else:
        return render(request,"Guest/Login.html")

def NewSeller(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        sellername=request.POST.get("txt_name")
        sellercontact=request.POST.get("txt_con")
        selleremail=request.POST.get("txt_email")
        sellerpassword=request.POST.get("txt_pass")
        sellerconfpassword=request.POST.get("txt_confpass")
        sellerestablishdate=request.POST.get("txt_date")
        sellerlicenseno=request.POST.get("txt_licenseno")
        sellerownername=request.POST.get("txt_ouwnername")
        sellerlicenseproof=request.FILES.get("txt_licenseproof")
        selleridproof=request.FILES.get("txt_idproof")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))  
        tbl_seller.objects.create(seller_name=sellername,seller_contactno=sellercontact,seller_email=selleremail,seller_password=sellerpassword,seller_establishdate=sellerestablishdate,seller_Licenseno=sellerlicenseno,seller_ownername=sellerownername,seller_licenseproof=sellerlicenseproof,seller_idproof=selleridproof,place=place)  
        return render(request,"Guest/NewSeller.html",{'msg':"Data inserted"})
    else:
        return render(request,"Guest/NewSeller.html",{'districtdata':districtdata,'placedata':placedata})
def WorkerRegistration(request):
    workerdata=tbl_worker.objects.all()
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Email=request.POST.get("txt_email")
        Contact=request.POST.get("txt_contact")
        Address=request.POST.get("txt_address")
        Photo=request.FILES.get("txt_photo")
        Proof=request.FILES.get("txt_proof")
        Password=request.POST.get("txt_password")
        workercount=tbl_worker.objects.filter(worker_email=Email).count()
        if workercount>0:
            return render(request,"Guest/WorkerRegistration.html",{'msg':"Worker Already exist"})
        else:
            tbl_worker.objects.create(worker_name=Name,worker_email=Email,worker_contact=Contact,worker_address=Address,worker_photo=Photo,worker_proof=Proof,worker_password=Password)
        return render(request,"Guest/WorkerRegistration.html",{'msg':"Registration Successfull"})
    else:
        return render(request,"Guest/WorkerRegistration.html",{'workerdata':workerdata})
def delworker(request,wid):
    tbl_worker.objects.get(id=wid).delete()
    return redirect("Guest:WorkerRegistration")   
def editworker(request,wid):
    editworker=tbl_worker.objects.get(id=wid)
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Email=request.POST.get("txt_email")
        Contact=request.POST.get("txt_contact")
        Address=request.POST.get("txt_address")
        Photo=request.FILES.get("txt_photo")
        Proof=request.FILES.get("txt_proof")
        Password=request.POST.get("txt_password")
        editworker.worker_name=Name
        editworker.worker_email=Email
        editworker.worker_contact=Contact
        editworker.worker_address=Address
        editworker.worker_photo=Photo
        editworker.worker_proof=Proof
        editworker.worker_password=Password
        if Photo:
            editworker.worker_photo=Photo
        if Proof:
            editworker.worker_proof=Proof
        editworker.save()
        return redirect("Guest:WorkerRegistration")
    else:
        return render(request,"Guest/WorkerRegistration.html/",{'editworker':editworker})
def Index(request):
    return render(request,"Guest/Index.html")

from django.shortcuts import render,redirect
from Admin.models import *
from worker.models import *
from Guest.models import *
from User.models import *
# Create your views here.
def Profile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/Profile.html",{'Data':profiledata})
def EditProfile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            contact=request.POST.get('txt_contact')
            houseno=request.POST.get('txt_hno')
            address=request.POST.get('txt_address')
            photo=request.FILES.get("txt_photo")
            profiledata.user_name=name
            profiledata.user_email=email
            profiledata.user_contactno=contact
            profiledata.user_houseno=houseno
            profiledata.user_address=address
            if photo:
                profiledata.user_photo=photo
            profiledata.save()
            return render(request,"User/EditProfile.html",{'msg':'Updated'})
        else:
            return render(request,"User/EditProfile.html",{'Data':profiledata})
def ChangePassword(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_user.objects.get(id=request.session['uid'])
        dbpass=profiledata.user_password
        if request.method=="POST":
            old=request.POST.get('txt_old')
            new=request.POST.get('txt_new')
            confirm=request.POST.get('txt_re')
            if old==dbpass:
                if new==confirm:
                    profiledata.user_password=new
                    profiledata.save()
                    return render(request,"User/ChangePassword.html",{'msg':'password changed'})
                else:
                    return render(request,"User/ChangePassword.html",{'msg':'New password mismatch'})
            else:
                return render(request,"User/ChangePassword.html",{'msg':'Old password incorrect'})
        else:
            return render(request,"User/ChangePassword.html",{'Data':profiledata})
def HomePage(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/HomePage.html",{'Data':userdata})
def Complaint(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        complaintdata=tbl_complaint.objects.filter(user=request.session['uid'])
        userdata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            title=request.POST.get("txt_title")
            content=request.POST.get("txt_content")
            tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
            return render(request,"User/Complaint.html",{'msg':"Data inserted"})
        else:
            return render(request,"User/Complaint.html",{'complaintdata':complaintdata})
def delcomplaint(request,cid):
    tbl_complaint.objects.get(id=cid).delete()
    return redirect("User:Complaint")
def Waste(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userId=tbl_user.objects.get(id=request.session['uid'])
        wastedata=tbl_waste.objects.filter(user_id=userId)
        categorydata=tbl_wastecategory.objects.all()
        if request.method=="POST":
            quantity=request.POST.get("txt_quantity")
            userdata=tbl_user.objects.get(id=request.session['uid'])
            waste=tbl_wastecategory.objects.get(id=request.POST.get("sel_wastecat"))
            wastecount=tbl_wastecategory.objects.filter(wastecategory_name=waste).count()
            tbl_waste.objects.create(waste_qty=quantity,wastecategory_id=waste,user_id=userdata)
            return render(request,"User/Waste.html",{'msg':"Data inserted"})
        else:
            return render(request,"User/Waste.html",{'wastedata':wastedata,'categorydata':categorydata})

def viewwardworker(request):
    user = tbl_user.objects.get(id=request.session['uid'])

    assignments = tbl_assignward.objects.filter(ward_id=user.ward_id)

    workers = tbl_worker.objects.filter(
        id__in=assignments.values_list('worker_id', flat=True)
    )
    # print(workers)
    return render(request,'User/ViewWardWorker.html',{'data':workers})

def delwaste(request,did):
    tbl_waste.objects.get(id=did).delete()
    return redirect("User:Waste")
def Feedback(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userId=tbl_user.objects.get(id=request.session['uid'])
        feedbackdata=tbl_feedback.objects.filter(user_id=userId)
        if request.method=="POST":
            content=request.POST.get("txt_content")
            userdata=tbl_user.objects.get(id=request.session['uid'])
            tbl_feedback.objects.create(feedback_content=content,user_id=userdata)
            return render(request,"User/Feedback.html",{'msg':"Data inserted"})
        else:
            return render(request,"User/Feedback.html",{'feedbackdata':feedbackdata})
def delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:Feedback")
def Payment(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userId=tbl_user.objects.get(id=request.session['uid'])
        paymentdata=tbl_payment.objects.filter(user_id=userId)
        if request.method=="POST":
            tbl_payment.objects.create(user_id=userId,payment_status=1)
            return render(request,"User/Payment.html",{'msg':' Payment Successfull'})
        else:
            return render(request,"User/Payment.html",{'paymentdata':paymentdata})

def ViewWasteStatus(request):
    uid = request.session["uid"]
    waste = tbl_waste.objects.filter(user_id=uid)
    return render(request,"User/ViewWasteStatus.html",{'waste':waste})

def Logout(request):
    del request.session['uid']
    return redirect("Guest:Login")


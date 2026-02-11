from django.shortcuts import render,redirect
from Admin.models import *
from worker.models import *
from Guest.models import *
from User.models import *
# Create your views here.

import requests

def get_current_location():
    
    response = requests.get("https://ipinfo.io/json")
    data = response.json()

    lat, lon = map(float, data["loc"].split(","))
    return {
        "latitude": lat,
        "longitude": lon,
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "ip": data.get("ip")
    }



def WorkerHomePage(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        location = get_current_location()
        print(location)
        workerdata=tbl_worker.objects.get(id=request.session['wid'])
        workerdata.worker_latitude=location['latitude']
        workerdata.worker_longitude=location['longitude']
        region=str(location['region'])
        country=str(location['country'])
        loc=region+", "+country
        workerdata.worker_curr_city=loc
        workerdata.save()
        workerdata.worker_curr_city=6

        assignwardata=tbl_assignward.objects.filter(worker_id=request.session['wid']).count()
        if assignwardata>0:
            return render(request,"worker/WorkerHomePage.html",{'status':'1'})
        else:
            return render(request,"worker/WorkerHomePage.html",{'Data':workerdata})
def Profile(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_worker.objects.get(id=request.session['wid'])
        assignwardata=tbl_assignward.objects.filter(worker_id=request.session['wid']).last()
        return render(request,"worker/Profile.html",{'Data':profiledata,'assignwardata':assignwardata})
def EditProfile(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_worker.objects.get(id=request.session['wid'])
        if request.method=="POST":
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            contact=request.POST.get('txt_contact')
            photo=request.FILES.get("txt_photo")
            profiledata.worker_name=name
            profiledata.worker_email=email
            profiledata.worker_contact=contact
            if photo:
                profiledata.worker_photo=photo
            profiledata.save()
            return render(request,"worker/EditProfile.html",{'msg':'Updated'})
        else:
            return render(request,"worker/EditProfile.html",{'Data':profiledata})
def ChangePassword(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_worker.objects.get(id=request.session['wid'])
        dbpass=profiledata.worker_password
        if request.method=="POST":
            old=request.POST.get('txt_old')
            new=request.POST.get('txt_new')
            confirm=request.POST.get('txt_re')
            if old==dbpass:
                if new==confirm:
                    profiledata.worker_password=new
                    profiledata.save()
                    return render(request,"worker/ChangePassword.html",{'msg':'password changed'})
                else:
                    return render(request,"worker/ChangePassword.html",{'msg':'New password mismatch'})
            else:
                return render(request,"worker/ChangePassword.html",{'msg':'Old password incorrect'})
        else:
            return render(request,"worker/ChangePassword.html",{'Data':profiledata})
def Attendence(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        workerId=tbl_worker.objects.get(id=request.session['wid'])
        tbl_workerattendence.objects.create(worker_id=workerId,workerattendence_status=1)
        return render(request,"worker/WorkerHomePage.html",{'msg':' Attendence Marked'})
def MyAttendence(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        workerId=tbl_worker.objects.get(id=request.session['wid'])
        workerdata=tbl_workerattendence.objects.filter(workerattendence_status=1,worker_id=workerId)
        return render(request,"worker/MyAttendence.html",{'workerdata':workerdata})
def delattendence(request,did):
    tbl_workerattendence.objects.get(id=did).delete()
    return redirect("worker:MyAttendence")

def ViewWaste(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        assignwardata = tbl_assignward.objects.filter(worker_id=request.session['wid']).last()
        wastedata = tbl_waste.objects.filter(user_id__ward_id=assignwardata.ward_id)  
        return render(request, "worker/ViewWaste.html", {'wastedata': wastedata})

def Collect(request,cid):
    data=tbl_waste.objects.get(id=cid)
    data.waste_status=1
    data.save()
    return render(request,"worker/Viewwaste.html",{'msg':'Collected'})
def ViewCollectionHistory(request):
    if "wid" not in request.session:
        return redirect("Guest:Login")
    else:
        assignwardata = tbl_assignward.objects.filter(worker_id=request.session['wid']).last()
        wastedata=tbl_waste.objects.filter(waste_status=1,user_id__ward_id=assignwardata.ward_id)
        return render(request,"worker/ViewCollectionHistory.html",{'wastedata':wastedata})

def WorkerMyAttendance(request):

    if "wid" not in request.session:
        return redirect("Guest:Login")

    worker = tbl_worker.objects.get(id=request.session['wid'])
    report = None
    total_present = 0
    total_absent = 0

    if request.method == "POST":
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")

        report = tbl_workerattendence.objects.filter(
            worker_id=worker,
            workerattendence_datetime__range=[from_date, to_date]
        )

    else:
        # Show all attendance by default
        report = tbl_workerattendence.objects.filter(
            worker_id=worker
        )

    total_present = report.filter(workerattendence_status=1).count()
    total_absent = report.filter(workerattendence_status=0).count()

    return render(request, "worker/WorkerMyAttendance.html", {
        "report": report,
        "total_present": total_present,
        "total_absent": total_absent
    })
        
def Logout(request):
    del request.session['wid']
    return redirect("Guest:Login")

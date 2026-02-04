from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from worker.models import *
from django.utils import timezone
from datetime import date
from django.conf import settings
from django.core.mail import send_mail

def District(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("txt_dis")
        tbl_district.objects.create(district_name=district)
        return render(request,"Admin/District.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/District.html",{'districtdata':districtdata})
def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("cat_name")
        tbl_category.objects.create(category_name=category)
        return render(request,"Admin/Category.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/Category.html",{'categorydata':categorydata})
def AdminRegistration(request):
    adminregistrationdata=tbl_adminregistration.objects.all()
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_pass")
        admincount=tbl_adminregistration.objects.filter(admin_email=Email).count()
        if admincount>0:
            return render(request,"Admin/AdminRegistration.html",{'msg':"Email already exist"})
        else:
            tbl_adminregistration.objects.create(admin_name=Name,admin_email=Email,admin_password=Password)
        return render(request,"Admin/AdminRegistration.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/AdminRegistration.html",{'adminregistrationdata':adminregistrationdata})
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")
def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("Admin:Category")
def deladminregistration(request,did):
    tbl_adminregistration.objects.get(id=did).delete()
    return redirect("Admin:AdminRegistration")
def editdistrict(request,did):
    editdata=tbl_district.objects.get(id=did)
    if request.method=="POST":
        district=request.POST.get("txt_dis")
        editdata.district_name=district
        editdata.save()
        return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html/",{'editdata':editdata})
def editcategory(request,did):
    editdata=tbl_category.objects.get(id=did)
    if request.method=="POST":
        category=request.POST.get("cat_name")
        editdata.category_name=category
        editdata.save()
        return redirect("Admin:Category")
    else:
        return render(request,"Admin/Category.html/",{'editdata':editdata})
def editadminregistration(request,did):
    editdata=tbl_adminregistration.objects.get(id=did)
    if request.method=="POST":
        adminname=request.POST.get("txt_name")
        adminemail=request.POST.get("txt_email")
        adminpassword=request.POST.get("txt_pass")
        editdata.admin_name=adminname
        editdata.admin_email=adminemail
        editdata.admin_password=adminpassword
        editdata.save()
        return redirect("Admin:AdminRegistration")
    else:
        return render(request,"Admin/AdminRegistration.html/",{'editdata':editdata})
def Place(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        place=request.POST.get("txt_place")
        district=tbl_district.objects.get(id=request.POST.get("sel_dist"))
        tbl_place.objects.create(place_name=place,district=district)
        return render(request,"Admin/Place.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/Place.html",{'districtdata':districtdata,'placedata':placedata})
def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")   
def editplace(request,did):
    districtdata=tbl_district.objects.all()
    editplace=tbl_place.objects.get(id=did)
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("sel_dist"))
        place=request.POST.get("txt_place")
        editplace.district=district
        editplace.place_name=place
        editplace.save()
        return redirect("Admin:Place")
    else:
        return render(request,"Admin/Place.html/",{'editplace':editplace,'districtdata':districtdata})
def Subcategory(request):
    categorydata=tbl_category.objects.all()
    subcatdata=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("txt_sub")
        category=tbl_category.objects.get(id=request.POST.get("sel_cat"))
        tbl_subcategory.objects.create(subcat_name=subcategory,category=category)
        return render(request,"Admin/Subcategory.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/Subcategory.html",{'categorydata':categorydata,'subcatdata':subcatdata})
def delsubcat(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("Admin:Subcategory")   
def editsubcat(request,did):
    categorydata=tbl_category.objects.all()
    editsubcat=tbl_subcategory.objects.get(id=did)
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get("sel_cat"))
        subcat=request.POST.get("txt_sub")
        editsubcat.category=category
        editsubcat.subcat_name=subcat
        editsubcat.save()
        return redirect("Admin:Subcategory")
    else:
        return render(request,"Admin/Subcategory.html",{'editsubcat':editsubcat,'categorydata':categorydata})
def Department(request):
    departmentdata=tbl_department.objects.all()
    if request.method=="POST":
        department=request.POST.get("txt_dep")
        tbl_department.objects.create(department_name=department)
        return render(request,"Admin/Department.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/Department.html",{'departmentdata':departmentdata})
def deldepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect("Admin:Department")
def editdepartment(request,did):
    editdata=tbl_department.objects.get(id=did)
    if request.method=="POST":
        department=request.POST.get("txt_dep")
        editdata.department_name=department
        editdata.save()
        return redirect("Admin:Department")
    else:
        return render(request,"Admin/Department.html/",{'editdata':editdata})
def Designation(request):
    designationdata=tbl_designation.objects.all()
    if request.method=="POST":
        designation=request.POST.get("txt_des")
        tbl_designation.objects.create(designation_name=designation)
        return render(request,"Admin/Designation.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/Designation.html",{'designationdata':designationdata})
def deldesignation(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect("Admin:Designation")
def editdesignation(request,did):
    editdata=tbl_designation.objects.get(id=did)
    if request.method=="POST":
        designation=request.POST.get("txt_des")
        editdata.designation_name=designation
        editdata.save()
        return redirect("Admin:Designation")
    else:
        return render(request,"Admin/Designation.html/",{'editdata':editdata})
def Employee(request):
    departmentdata=tbl_department.objects.all()
    designationdata=tbl_designation.objects.all()
    employeedata=tbl_employee.objects.all()
    if request.method=="POST":
        empname=request.POST.get("txt_name")
        empgender=request.POST.get("txt_gender")
        empcontact=request.POST.get("txt_con")
        empdob=request.POST.get("txt_dob")
        empsalary=request.POST.get("txt_sal")
        department=tbl_department.objects.get(id=request.POST.get("sel_dep"))
        designation=tbl_designation.objects.get(id=request.POST.get("sel_des"))
        tbl_employee.objects.create(employee_name=empname,employee_gender=empgender,employee_contact=empcontact,employee_dob=empdob,employee_salary=empsalary,department=department,designation=designation)
        return render(request,"Admin/Employee.html",{'msg':"Data inserted"})
    else:
        return render(request,"Admin/Employee.html",{'employeedata':employeedata,'departmentdata':departmentdata,'designationdata':designationdata,})
def delemployee(request,did):
    tbl_employee.objects.get(id=did).delete()
    return redirect("Admin:Employee")   
def editemployee(request,did):
    departmentdata=tbl_department.objects.all()
    designationdata=tbl_designation.objects.all()
    editemployee=tbl_employee.objects.get(id=did)
    if request.method=="POST":
        department=tbl_department.objects.get(id=request.POST.get("sel_dep"))
        designation=tbl_designation.objects.get(id=request.POST.get("sel_des"))
        empname=request.POST.get("txt_name")
        empgender=request.POST.get("txt_gender")
        empcontact=request.POST.get("txt_con")
        empdob=request.POST.get("txt_dob")
        empsalary=request.POST.get("txt_sal")
        editemployee.department=department
        editemployee.designation=designation
        editemployee.employee_name=empname
        editemployee.employee_gender=empgender
        editemployee.employee_contact=empcontact
        editemployee.employee_dob=empdob
        editemployee.employee_salary=empsalary
        editemployee.save()
        return redirect("Admin:Employee")
    else:
        return render(request,"Admin/Employee.html/",{'editemployee':editemployee,'departmentdata':departmentdata,'designationdata':designationdata})
def UserList(request):
    admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
    userdata=tbl_user.objects.all()
    acceptdata=tbl_user.objects.filter(user_status=1)
    rejectdata=tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserList.html",{'Data':admindata,'userdata':userdata,'acceptdata':acceptdata,'rejectdata':rejectdata})
def SellerList(request):
    sellerdata=tbl_seller.objects.all()
    acceptdata=tbl_seller.objects.filter(seller_status=1)
    rejectdata=tbl_seller.objects.filter(seller_status=2)
    return render(request,"Admin/SellerList.html",{'sellerdata':sellerdata,'acceptdata':acceptdata,'rejectdata':rejectdata})
def acceptseller(request,aid):
    data=tbl_seller.objects.get(id=aid)
    data.seller_status=1
    data.save()
    return render(request,"Admin/SellerList.html",{'msg':'verified'})
def rejectseller(request,rid):
    data=tbl_seller.objects.get(id=rid)
    data.seller_status=2
    data.save()
    return render(request,"Admin/SellerList.html",{'msg':'Rejected'})
def acceptuser(request,aid):
    data=tbl_user.objects.get(id=aid)
    data.user_status=1
    data.save()
    email=data.user_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rWe are happy to inform you that your registration with ecobloom has been successfully approved by the administrator"
        "\r You can now log in to the system and access the available services, submit requests, and track waste collection activities in your ward "
        "\r if you face any issues while logging in or need further assistance, feel free to contact our support team.."
        "\r Thank you for being a part of ecobloom and supporting a cleaner, greener community."
        "\r Warm regards,"
        "\r Admin"
        "\r ecobloom" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/UserList.html",{'msg':'verified'})
def rejectuser(request,rid):
    data=tbl_user.objects.get(id=rid)
    data.user_status=2
    data.save()
    email=data.user_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rThank you for registering with ecobloom."
        "\r After careful review, we regret to inform you that your registration request has not been approved at this time. This may be due to incomplete information, invalid documents, or not meeting the required criteria."
        "\r You may update your details and submit a new request, or contact the administrator for further clarification"
        "\r We appreciate your interest in Haritha Karma Sena and encourage you to apply again"
        "\r Thank you for your understanding."
        "\r regards,"
        "\r Admin"
        "\r ecobloom" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/UserList.html",{'msg':'Rejected'})
def HomePage(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        return render(request,"Admin/HomePage.html",{'Data':admindata})
def ViewComplaint(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        viewcomplaintdata=tbl_complaint.objects.filter(complaint_status=0)
        replied=tbl_complaint.objects.filter(complaint_status=1)
        return render(request,"Admin/ViewComplaint.html",{'Data':admindata,'viewcomplaintdata':viewcomplaintdata,'replied':replied})
def Reply(request,cid):
    admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
    complaintdata=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        reply=request.POST.get("txt_reply")
        complaintdata.complaint_reply=reply
        complaintdata.complaint_status=1
        complaintdata.save()
        return render(request,"Admin/Reply.html",{'msg':'Replied'})
    else:
         return render(request,"Admin/Reply.html",{'Data':admindata})
def Ward(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        warddata=tbl_ward.objects.all()
        if request.method=="POST":
            wardno=request.POST.get("txt_ward")
            wardcount=tbl_ward.objects.filter(ward_number=wardno).count()
            if wardcount>0:
                return render(request,"Admin/Ward.html",{'msg':"Ward already exist"})
            else:
                tbl_ward.objects.create(ward_number=wardno)
            return render(request,"Admin/Ward.html",{'msg':"Data inserted"})
        else:
            return render(request,"Admin/Ward.html",{'Data':admindata,'warddata':warddata})
def delward(request,wid):
    tbl_ward.objects.get(id=wid).delete()
    return redirect("Admin:Ward")
def WorkerVerification(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        workerdata=tbl_worker.objects.all()
        acceptdata=tbl_worker.objects.filter(worker_status=1)
        rejectdata=tbl_worker.objects.filter(worker_status=2)
        return render(request,"Admin/WorkerVerification.html",{'Data':admindata,'workerdata':workerdata,'acceptdata':acceptdata,'rejectdata':rejectdata})
def acceptworker(request,aid):
    data=tbl_worker.objects.get(id=aid)
    data.worker_status=1
    data.save()
    email=data.worker_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rWe are happy to inform you that your registration with ecobloom has been successfully approved by the administrator"
        "\r You can now log in to the system and access the available services, submit requests, and track waste collection activities in your ward "
        "\r if you face any issues while logging in or need further assistance, feel free to contact our support team.."
        "\r Thank you for being a part of ecobloom and supporting a cleaner, greener community."
        "\r Warm regards,"
        "\r Admin"
        "\r ecobloom" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/WorkerVerification.html",{'msg':'verified'})
def rejectworker(request,rid):
    data=tbl_worker.objects.get(id=rid)
    data.worker_status=2
    data.save()
    email=data.worker_email
    send_mail(
          'Respected Sir/Madam ',#subject
        "\rThank you for registering with ecobloom."
        "\r After careful review, we regret to inform you that your registration request has not been approved at this time. This may be due to incomplete information, invalid documents, or not meeting the required criteria."
        "\r You may update your details and submit a new request, or contact the administrator for further clarification"
        "\r We appreciate your interest in Haritha Karma Sena and encourage you to apply again"
        "\r Thank you for your understanding."
        "\r regards,"
        "\r Admin"
        "\r ecobloom" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"Admin/WorkerVerification.html",{'msg':'Rejected'})
def WasteCategory(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        wastecategorydata=tbl_wastecategory.objects.all()
        if request.method=="POST":
            wastecategory=request.POST.get("txt_wastecategory")
            wastecount=tbl_wastecategory.objects.filter(wastecategory_name=wastecategory).count()
            if wastecount>0:
                return render(request,"Admin/WasteCategory.html",{'msg':"Waste category already exist"})
            else:
                tbl_wastecategory.objects.create(wastecategory_name=wastecategory)
            return render(request,"Admin/WasteCategory.html",{'msg':"Data inserted"})
        else:
            return render(request,"Admin/WasteCategory.html",{'Data':admindata,'wastecategorydata':wastecategorydata})
def delwastecategory(request,did):
    tbl_wastecategory.objects.get(id=did).delete()
    return redirect("Admin:WasteCategory")
def ViewWorker(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        workerdata=tbl_worker.objects.filter(worker_status=1)
        return render(request,"Admin/ViewWorker.html",{'Data':admindata,'workerdata':workerdata})
def AssignWard(request,wid):
    admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
    warddata=tbl_ward.objects.all()
    assignward = tbl_assignward.objects.filter(worker_id=wid)
    workerdata=tbl_worker.objects.get(id=wid)
    if request.method=="POST":
        ward=tbl_ward.objects.get(id=request.POST.get("sel_ward"))
        assignwardcount=tbl_assignward.objects.filter(ward_id=ward,worker_id=workerdata).count()
        if assignwardcount>0:
            return render(request,"Admin/AssignWard.html",{'msg':"Ward already assigned",'wid':wid})
        else:
            tbl_assignward.objects.create(ward_id=ward,worker_id=workerdata)
        return render(request,"Admin/AssignWard.html",{'msg':"Data inserted",'wid':wid})
    else:
        return render(request,"Admin/AssignWard.html",{'Data':admindata,'warddata':warddata,'assignward':assignward,'wid':wid})
def delassignedward(request,wid,did):
    tbl_assignward.objects.get(id=did).delete()
    return redirect("Admin:AssignWard",wid)   
def ViewFeedback(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        feedbackdata=tbl_feedback.objects.all()
        return render(request,"Admin/ViewFeedback.html",{'Data':admindata,'feedbackdata':feedbackdata})
def Logout(request):
    del request.session['aid']
    return redirect("Guest:Login")

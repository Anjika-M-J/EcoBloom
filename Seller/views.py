from django.shortcuts import render
from Guest.models import *
from Seller.models import *
# Create your views here.
def SellerHomePage(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/SellerHomePage.html",{'Data':sellerdata})
def SellerProfile(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/SellerProfile.html",{'Data':profiledata})
def SellerEditProfile(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        establishdate=request.POST.get('txt_estbdate')
        licenseno=request.POST.get('txt_lno')
        licensproof=request.POST.get('txt_lp')
        idproof=request.POST.get('txt_ip')
        ownername=request.POST.get('txt_on')
        profiledata.seller_name=name
        profiledata.seller_email=email
        profiledata.seller_contactno=contact
        profiledata.seller_establishdate=establishdate
        profiledata.seller_Licenseno=licenseno
        profiledata.seller_ownername=ownername
        profiledata.save()
        return render(request,"Seller/SellerEditProfile.html",{'msg':'Updated'})
    else:
        return render(request,"Seller/SellerEditProfile.html",{'Data':profiledata})
def SellerChangePassword(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    dbpass=profiledata.seller_password
    if request.method=="POST":
        old=request.POST.get('txt_old')
        new=request.POST.get('txt_new')
        confirm=request.POST.get('txt_re')
        if old==dbpass:
            if new==confirm:
                profiledata.seller_password=new
                profiledata.save()
                return render(request,"Seller/SellerChangePassword.html",{'msg':'password changed'})
            else:
                return render(request,"Seller/SellerChangePassword.html",{'msg':'New password mismatch'})
        else:
            return render(request,"Seller/SellerChangePassword.html",{'msg':'Old password incorrect'})
    else:
        return render(request,"Seller/SellerChangePassword.html",{'Data':profiledata})
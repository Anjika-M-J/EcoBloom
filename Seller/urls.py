from django.urls import path
from Seller import views
app_name="Seller"
urlpatterns = [
    path('SellerProfile/',views.SellerProfile,name="SellerProfile"),
    path('SellerEditProfile/',views.SellerEditProfile,name="SellerEditProfile"),
    path('SellerChangePassword/',views.SellerChangePassword,name="SellerChangePassword"),
    path('SellerHomePage/',views.SellerHomePage,name="SellerHomePage")
]
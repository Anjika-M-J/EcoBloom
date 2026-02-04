from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('Profile/',views.Profile,name="Profile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('HomePage/',views.HomePage,name="HomePage"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('delcomplaint/<int:cid>',views.delcomplaint,name="delcomplaint"),
    path('Waste/',views.Waste,name="Waste"),
    path('viewwardworker/',views.viewwardworker,name="viewwardworker"),
    path('delwaste/<int:did>',views.delwaste,name="delwaste"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('delfeedback/<int:did>',views.delfeedback,name="delfeedback"),
    path('Payment/',views.Payment,name="Payment"),
    path('ViewWasteStatus/',views.ViewWasteStatus,name="ViewWasteStatus"),
    path('Logout/',views.Logout,name="Logout")    
]
from django.urls import path
from worker import views
app_name="worker"
urlpatterns = [
    path('WorkerHomePage/',views.WorkerHomePage,name="WorkerHomePage"),
    path('Profile/',views.Profile,name="Profile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Attendence/',views.Attendence,name="Attendence"),
    path('MyAttendence/',views.MyAttendence,name="MyAttendence"),
    path('delattendence/<int:did>',views.delattendence,name="delattendence"),
    path('ViewWaste/',views.ViewWaste,name="ViewWaste"),
    path('Collect/<int:cid>',views.Collect,name="Collect"),
    path('ViewCollectionHistory/',views.ViewCollectionHistory,name="ViewCollectionHistory"),
    path('Logout/',views.Logout,name="Logout")
]
    
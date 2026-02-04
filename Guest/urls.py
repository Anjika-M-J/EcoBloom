from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('NewUser/',views.NewUser,name="NewUser"),
    path('AjaxPlace/',views.AjaxPlace,name='AjaxPlace'),
    path('Login/',views.Login,name="Login"),
    path('NewSeller/',views.NewSeller,name="NewSeller"),
    path('WorkerRegistration/',views.WorkerRegistration,name="WorkerRegistration"),
    path('delworker/<int:wid>',views.delworker,name="delworker"),
    path('editworker/<int:wid>',views.editworker,name="editworker"),
    path('Index/',views.Index,name="Index"),
]
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="profiles/memberlogin.html"), name="nameMemberLogin"),
    path('updateProfile/', views.ProfileEditView.as_view(), name='nameUpdateProfile'),
    path('register/', views.SiteRegisterView.as_view(), name='nameMemberRegister'),
    path('registerOk/', views.SiteResgisterOkView.as_view(), name='register_ok'),
    path('logout/', views.SiteLogoutView.as_view(), name='nameMemberlogout'),
    path('inforProfiles/', views.ProfilesContent.as_view(), name='nameInforProfile')
]

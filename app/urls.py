from django.urls import path, include
from . import views

# urlpatterns = [
#     path("",views.RegisterPage,name="registerpage"), 
#     path("register/",views.UserRegister,name="register"),   
#     path("loginpage/",views.LoginPage,name="loginpage"),
#     path("loginuser/",views.LoginUser,name="login"),
# ]

# urlpatterns = [
#     path('', views.login_view, name='login'),
#     path('home/', views.home_view, name='home'),
#     path('logout/', views.logout_view, name='logout'),
    
# ]

urlpatterns = [
    path('', views.login_view, name='root'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='accounts-login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
]

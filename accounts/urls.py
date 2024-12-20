from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('signup/',views.signupPage,name="signup"),
    path('forgot_password/',views.forgotPasswordPage,name="forgot_password"),
    path('change_password/',views.changePasswordPage,name="change_password"),
    path('dashboard/',views.dashboardPage,name="dashboard"),
    path('profile/',views.profilePage,name="profile"),
]
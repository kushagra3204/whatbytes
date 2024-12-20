from django.shortcuts import render

def loginPage(request):
    return render(request,"login.html")

def signupPage(request):
    return render(request,"signup.html")

def forgotPasswordPage(request):
    return render(request,"forgotPassword.html")

def changePasswordPage(request):
    return render(request,"changePassword.html")

def dashboardPage(request):
    return render(request,"dashboard.html")

def profilePage(request):
    return render(request,"profile.html")
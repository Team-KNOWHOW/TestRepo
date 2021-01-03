from django.shortcuts import render, redirect

def login(request):
    return render(request, "login.html")

def member_register(request):
    return render(request, "member_register.html")

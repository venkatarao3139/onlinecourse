from django.shortcuts import render,redirect
from django.contrib import messages
def homepage(request):
    return render(request,"home_page.html")


def adminpage(request):
    return render(request,"admin_page.html")


def studentpage(request):
    return render(request,"student_page.html")


def adminhomepage(request):
        user = request.POST.get("us")
        pswrd = request.POST.get("ps")
        if user=="venkat" and pswrd=="venky3139":
            return render(request,"admin_home_page.html")
        else:
            return render(request,'admin_page.html',{"data":"invalid Details"})


def register_page(request):
    return render(request,"register_page.html")


def Student_login(request):
    return render(request,"Student_login.html")
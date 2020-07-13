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
            messages.error(request,"invlid username or password")
            return redirect('admin1')

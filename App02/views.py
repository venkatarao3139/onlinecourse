from django.shortcuts import render,redirect
from django.contrib import messages
from App02.models import Student_register,ScheduleNewClass
from django.views.generic import UpdateView,DeleteView
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
            return render(request,'admin_page.html',{"data":"INVALID ADMIN DETAILS"})

def register_page(request):
    return render(request,"register_page.html")

def Student_login(request):
    return render(request,"Student_login.html")

def savestdent(request):
    name = request.POST.get("t1")
    cont = request.POST.get("t2")
    email = request.POST.get("t3")
    usr = request.POST.get("t4")
    psr = request.POST.get("t5")
    Student_register(Name=name,contact=cont,email=email,user=usr,password=psr).save()
    messages.success(request," Student Data is Saved")
    return redirect('register')

def newcource(request):
    return render(request,"newc_ource.html")

def svaecourse(request):
    name = request.POST.get("c1")
    fclty = request.POST.get("c2")
    edate = request.POST.get("c3")
    etime = request.POST.get("c4")
    fee = request.POST.get("c5")
    dur = request.POST.get("c6")
    ScheduleNewClass(cname=name,Faculty=fclty,Date=edate,Time=etime,Fee=fee,Duration=dur).save()
    messages.success(request,"New course is Saved ")
    return redirect('newcource')

def courseslist(request):
    coureses = ScheduleNewClass.objects.all()
    return render(request,"list_of_courses.html",{"data":coureses})

def studentlogin_home(request):
    id = request.POST.get("use")
    word = request.POST.get("psw")
    std = Student_register.objects.get(user=id,password=word)
    if id==std.user and word==std.password:
        return redirect("student_home")
    else:
        return render(request, "Student_login.html", {"eror": "INVALID STUDENT DETAILS"})

def student_home(request):
    return render(request,"student_home.html")


class Updatecourse(UpdateView):
    template_name = "update_course.html"
    model = ScheduleNewClass
    fields = "__all__"
    success_url = "/courseslist/"


class Remove_course(DeleteView):
    template_name = "Delete_course.html"
    model = ScheduleNewClass
    fields = "__all__"
    success_url = "/courseslist/"


def student_list(request):
   student = Student_register.objects.all()
   return render(request, "students_list.html", {"std": student})

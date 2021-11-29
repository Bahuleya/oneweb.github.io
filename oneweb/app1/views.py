from django.shortcuts import render,redirect
from .models import Student
from .form import Stu_Form

# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def allrecord(request):
    sf=Student.objects.all()
    di={'sf':sf}

    return render(request,'app1/allrecord.html',di)

def insert(request):
    s_form=Stu_Form()
    di={'s_form':s_form}
    if request.method=="POST":
        sform=Stu_Form(request.POST)
        if sform.is_valid():
            sform.save(commit=True)
            return redirect('/allrecord/')

    return render(request,'app1/insert.html',di)

def update(request,sno):
    sf = Student.objects.get(sno=sno)
    di = {'sf': sf}
    if request.method=="POST":
        sform = Stu_Form(request.POST,instance=sf)
        if sform.is_valid():
            print('update form is valid')
            sform.save(commit=True)
            return redirect('/allrecord/')
    return render(request,'app1/update.html',di)

def delete (reqeust,sno):
    sf=Student.objects.get(sno=sno)
    sf.delete()
    return redirect('/allrecord/')




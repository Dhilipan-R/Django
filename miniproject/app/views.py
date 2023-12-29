from django.shortcuts import render,redirect
from .models import employee
# Create your views here

def index(request):
    data=employee.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    data=employee.objects.all()
    context={"data":data}
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=employee(email=email,name=name,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html",context)

def updateData(request,id):
    
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        edit=employee.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
     
        return redirect("/")
    d=employee.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=employee.objects.get(id=id)
    d.delete()
    return redirect("/")
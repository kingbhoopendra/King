from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from doctor.forms import Employeeform
# Create your views here.
def demo(request):
    return HttpResponse("<h1 style='color:red;'> WELCOME TO MY FIRST HOSPITAL PROJECT-DJANGO</h1>")
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def form(request):
	form=Employeeform()
	return render(request,'form.html',{"form":form})
# def adddata(request):
#  	if request.method == 'GET':
#  		name = request.GET['name']
#  		email = request.GET['email']
#  		mobile = request.GET['mob']
#  		salary = request.GET['sal']
#  		data = [name,email,mobile,salary]
#  		return HttpResponse(data)
# #def form2(request):
# 	return render(request, 'form2.html')
# def adddata2(request):
# 	if request.method == 'POST':
# 			name = request.POST['name']
# 			email = request.POST['email']
# 			mobile = request.POST['mob']
# 			salary = request.POST['sal']
# 			data = [name, email, mobile, salary]
# 			return HttpResponse(data)
def adddata(request):
	if request.method == 'POST':
		form=Employeeform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse('data inserted')
	else:
		form=Employeeform()
		return render(request,'form.html',{'form':form})
def getdata(request):
	   data=Employee.objects.all()
	   return render(request,'show.html',{'data':data})
def delete(request, id):
	   # return HttpResponse(id)
		data = Employee.objects.get(id=id)
		data.delete()
		return redirect('/getdata/')
def getdataforedit(request,id):

	   data = Employee.objects.get(id=id)
	   return render(request,'editdata.html',{'data':data})

def update(request,id):
	if request.method == "GET":
		emp = Employee.objects.get(id=id)
		form = Employeeform(request.GET,instance=emp)
		if form.is_valid():
			try:
				form.save()
				return redirect('/getdata')
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request,"editdata.html",{'form':form})



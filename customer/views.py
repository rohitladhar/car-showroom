from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import Bookcar,Business,Service,Car,Bookservice
from django.contrib.auth.models import User,auth,Group
from .forms import BusinessForm,ServiceForm,LoginForm,CustomerBillForm,ServiceBillForm,MemberForm
from django.contrib import messages
from django.db.models import CharField, Case, Value, When ,Q,F
from sales.models import Newservice,Newcustomer
from django.template.loader import get_template
from io import BytesIO
from django.db.models import Q
from xhtml2pdf import pisa
from expenditure.models import EmployeeDetail
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    cars=Car.objects.all()
    return render(request,"start.html",{'cars':cars})

def business(request):
    form = BusinessForm()
    message={'one':'Business Registration Form ','two':'Book a Meeting with us'}
    context={
        'message':message,
        'form':form,
    }
    return render(request,'business.html',context)

def service(request):
    form = ServiceForm()
    message={'one':'Service Registration Form ','two':'Book a Service'}
    context={
        'message':message,
        'form':form,
    }
    return render(request,'service.html',context)

def addbusiness(request):
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/')

def bookyourcar(request):
    if request.method == 'POST':
        name=request.POST['bycname']
        phone=request.POST["bycphone"]
        bmodel=request.POST["bycmodel"]
        email=request.POST["bycemail"]
        advance=request.POST["bycadvance"]
        date=request.POST["bycdate"]

        byccar=Bookcar(bycname=name,bycphone=phone,bycmodel=bmodel,bycemail=email,bycadvance=advance,bycdate=date)

        byccar.save()
        print('success')
        return HttpResponseRedirect('/')


def login(request):
    form=LoginForm()
    message={'one':'Staff Form ','two':'Input user credentials'}
    context={
        'message':message,
        'form':form,
    }
    return render(request,'login.html',context)


def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            str1=Group.objects.get(pk=1)
            str2=Group.objects.get(pk=2)
            
            if user.username==str1.name:
                
                return redirect('sales/sales_home')
            elif user.username==str2.name:
                return redirect('expenditure/expenditure_home')
            else:
                return redirect('employee/employee_home')

        else:
            messages.info(request,'Invalid user credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def bookservice(request):
    
    if request.method == "POST":
        date=request.POST['date']
        if Bookservice.object.filter(date=date).exists():
            date=updateservice(request,date)
            return date
        else:
            date=showservice(request,date)
            return date
    
    else:
        context={
        'mavailable':10,
        'mbooked':0,
        'ebooked':0,
        'eavailable':10,      
        }
        return render(request, 'bookservice.html',context)

def updateservice(request,date):
    cd=Bookservice.object.get(date=date)
    mavailable=cd.mavailable
    mbooked=cd.mbooked
    ebooked=cd.ebooked
    eavailable=cd.eavailable
    context={
        'mavailable':mavailable,
        'mbooked':mbooked,
        'ebooked':ebooked,
        'eavailable':eavailable,  
        'date':date,    
    }
    return render( request, 'bookservice.html',context)

def showservice(request,date):
    mavailable=10
    mbooked=0
    eavailable=10
    ebooked=0
    form=Bookservice(date=date,mavailable=mavailable,mbooked=mbooked,eavailable=eavailable,ebooked=ebooked)
    form.save()
    context={
        'mavailable':mavailable,
        'mbooked':mbooked,
        'ebooked':ebooked,
        'eavailable':eavailable, 
        'date':date,
    }
    return render( request, 'bookservice.html',context)

def servicevalue(request):
    if request.method == "POST":
        date=request.POST['mdate']
        slot=request.POST['slotm']
        context={
            "date":date,
            "slot":slot,
        }
        ab=Bookservice.object.get(date=date)
        avail=ab.mavailable
        book=ab.mbooked
        ab.mavailable=avail-1
        ab.mbooked=book+1
        ab.save()
        return render( request, 'servicebooking.html',context)
    else:
        date=request.GET['edate']
        slot=request.GET['slote']
        context={
            "date":date,
            "slot":slot,
        }
        ab=Bookservice.object.get(date=date)
        avail=ab.eavailable
        book=ab.ebooked
        ab.eavailable=avail-1
        ab.ebooked=book+1
        ab.save()
        return render( request, 'servicebooking.html',context)
        

def servicebooking(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST["phone"]
        email=request.POST["email"]
        date=request.POST["date"]
        slot=request.POST["slot"]
        reg=request.POST["reg"]

        obj=Service(sname=name,sphone=phone,sslot=slot,semail=email,sreg=reg,sdate=date)
        obj.save()
        return HttpResponseRedirect('/')
            

def backservice(request):
    date=0
    slot="morning"
        
    if slot=="morning":
        ab=Bookservice.object.get(date=date)
        avail=ab.mavailable
        book=ab.mbooked
        ab.mavailable=avail+1
        ab.mbooked=book-1
        ab.save()
        return render( request, 'bookservice.html')

    else:
        ab=Bookservice.object.get(date=date)
        avail=ab.eavailable
        book=ab.ebooked
        ab.eavailable=avail+1
        ab.ebooked=book+1
        ab.save()
        return render( request, 'bookservice.html')


def bill(request):
    
    context={
    'one':' ',
    'two':' ',
    
    }
    
    return render(request,'bill.html',context)


def customercheck(request):
    if request.method=='POST':
        unique=request.POST['unique']
        if Newcustomer.object.filter(cunique=unique).exists():
            unique=customerbill(request,unique)
            return unique
            
        else:
            context={
                'one':'Invalid Customer Unique Id',
                'two':''
            }
            return render(request,'bill.html',context)

    else:
        return render(request,'bill')

def servicecheck(request):
    if request.method=='POST':
        unique=request.POST['unique']
        if Newservice.object.filter(sunique=unique).exists():
            unique=servicebill(request,unique)
            return unique
            
        else:
            context={
                'one':'',
                'two':'Invalid Service Unique Id',
            }
            return render(request,'bill.html',context)

    else:
        return render(request,'bill')

def customerbill(request,unique):
    customer=Newcustomer.object.get(cunique=unique)
    
    context={
        'customer':customer,
        
    }
    template=get_template("customerbill.html")
    data_p=template.render(context)
    response=BytesIO()
    pdfpage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfpage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

def servicebill(request,unique):
    service=Newservice.object.get(sunique=unique)
    
    context={
        'service':service
    }
    
    template=get_template("servicebill.html")
    data_p=template.render(context)
    response=BytesIO()
    pdfpage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfpage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

def staff(request):
    form=MemberForm()
    message={'one':'Employee Login ','two':'Input user credentials'}
    context={
        'message':message,
        'form':form,
    }
    return render(request,'memberlogin.html',context)


def memberlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('employee/employee_home')

        else:
            messages.info(request,'Invalid user credentials')
            return redirect('staff')
    else:
        return render(request,'memberlogin.html')
    
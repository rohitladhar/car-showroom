from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from expenditure.models import Record,Application,EmployeeDetail
from django.db.models import Q
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
# Create your views here.

def employeehome(request):
   request.session['name']=request.user.username
   username=request.session['name']

   ab=Record.object.get(Q(rid=username),Q(rmonth='January'),Q(ryear='2020'))
   Jan_salary=ab.rtotal
   Jan_hour=ab.rhour
   Jan_over=ab.rover
   
   bc=Record.object.get(Q(rid=username),Q(rmonth='Febuary'),Q(ryear='2020'))
   Feb_salary=bc.rtotal
   Feb_hour=bc.rhour
   Feb_over=bc.rover
      
   cd=Record.object.get(Q(rid=username),Q(rmonth='March'),Q(ryear='2020'))
   Mar_salary=cd.rtotal
   Mar_hour=cd.rhour
   Mar_over=cd.rover
      
   de=Record.object.get(Q(rid=username),Q(rmonth='April'),Q(ryear='2020'))
   Apr_salary=de.rtotal
   Apr_hour=de.rhour
   Apr_over=de.rover
      
   context={
      'jan':Jan_salary,
      'feb':Feb_salary,
      'mar':Mar_salary,
      'apr':Apr_salary,
      'jhour':Jan_hour,
      'jover':Jan_over,
      'fhour':Feb_hour,
      'fover':Feb_over,
      'mhour':Mar_hour,
      'mover':Mar_over,
      'ahour':Apr_hour,
      'aover':Apr_over,
      'username':username
   }
   return render(request,"employee_home.html",context)

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return redirect('login')
   
def calculator(request):
   request.session['name']=request.user.username
   username=request.session['name']
   return render(request,"calculator.html",{'username':username})

def employeesalary(request):
   username=userid(request)
   return render(request,"employeesalary.html",{'username':username})

def recordcheck(request):
   request.session['name']=request.user.username
   username=request.session['name']
   if request.method=='POST':
      year=request.POST['year']
      month=request.POST['month']
      if Record.object.filter(Q(rid=username),Q(rmonth=month),Q(ryear=year)).exists():
         unique=salary(request,year,month)
         return unique
            
      else:
         context={
             'one':'No Record Found',
             'username':username
         }
         return render(request,'employeesalary.html',context)

   else:
      return render(request,'employeesalary')

def salary(request,year,month):
   request.session['name']=request.user.username
   username=request.session['name']
   salary=Record.object.get(Q(rid=username),Q(rmonth=month),Q(ryear=year))
    
   context={
        'salary':salary,
        
   }
   template=get_template("salary.html")
   data_p=template.render(context)
   response=BytesIO()
   pdfpage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
   if not pdfpage.err:
     return HttpResponse(response.getvalue(),content_type="application/pdf")
   else:
     return HttpResponse("Error Generating PDF")

def userid(request):
   request.session['name']=request.user.username
   username=request.session['name']
   return username

def employeeapplication(request):
   username=userid(request)
   if request.method=='POST':
      date=request.POST['date']
      desc=request.POST['desc']
      reason=request.POST['reason']
      if Application.object.filter(Q(empid=username),Q(date=date)).exists():
         date=showvalidation(request,date)
         return date

      else:
         status="Unchecked"
         app=Application(empid=username,date=date,desc=desc,reason=reason,status=status)
         app.save()
         context={
             'one':'Application is submitted',
             'username':username
         }
         return render(request,"employeeapplication.html",context)
         
   
   return render(request,"employeeapplication.html",{'username':username})

def showvalidation(request,date):
   username=userid(request)
   context={
             'two':'Only One Application per day is allowed',
             'username':username
         }
   return render(request,"employeeapplication.html",context)

def applicationstatus(request):
   
   username=userid(request)
   if request.method=='POST':
      date=request.POST['date']
      if Application.object.filter(Q(empid=username),Q(date=date)).exists():
         date=showstatus(request,date)
         return date
      else:
         context={
            'one':'No Record Found',
            'username':username
         }
         return render(request,"applicationstatus.html",context)
   context={
             
             'username':username
         }
   return render(request,"applicationstatus.html",context)

def showstatus(request,date):
   username=userid(request)
   ab=Application.object.get(Q(empid=username),Q(date=date))
   status=ab.status
   reason=ab.reason
   context={
            'username':username,
            'date':date,
            'status':status,
            'reason':reason,
         }
   return render(request,"applicationstatus.html",context)

def updateother(request):
   username=userid(request)
   if request.method=='POST':
      phone=request.POST['phone']
      email=request.POST['email']
      ab=EmployeeDetail.object.get(nid=username)
      ab.nphone=phone
      ab.nemail=email
      ab.save()
      context={
            'username':username,
            'one':'Record is Updated'
         }
      return render(request,"updateother.html",context)
   context={
            'username':username,
         }
   return render(request,"updateother.html",context)
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,get_object_or_404
from .forms import AddEmployee,AddRecord
from django.contrib.auth.models import User,auth,Group
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import EmployeeDetail,Record,Position,Application
from django.db.models import Sum,Count
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.

def expenditurehome(request):
    return render(request,"expenditure_home.html")

def logout(request):
    auth.logout(request)
    return redirect('login')

def user_id(nid):
    qs = EmployeeDetail.objects.filter(nid=nid)
    if qs.exists():
        return qs[0]
    return None

class AddEmployeeView(CreateView):
    model = EmployeeDetail
    template_name = 'addemployee.html'
    form_class = AddEmployee
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['one'] = 'Add New Employee'
        context['two'] = 'Provide User Details'
        return context

    def form_valid(self, form):
        form.instance.employee = user_id(self.request.user)
        form.save()
        return redirect(reverse("employee-detail"))

class AddRecordView(CreateView):
    model = Record
    template_name = 'addrecord.html'
    form_class = AddRecord
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['one'] = 'Add New Record'
        context['two'] = 'Provide User Details'
        return context

    def form_valid(self, form):
        record = form.save(commit=False)
        rid=form['rid'].value()
        hour=form['rhour'].value()
        over=form['rover'].value()
        leave=form['rleave'].value()
        absent=form['rabsent'].value()
        foul=form['rfoul'].value()
        allow=form['rallow'].value()
        ab=EmployeeDetail.objects.get(nid=rid)
        post=ab.npost
        name=ab.nname
        cd=Position.objects.get(post=post)
        pay=cd.pay
        record.rpost=post
        hourpay=pay*float(hour)
        record.rhour=hour
        record.rhoursum=hourpay
        overpay=pay*float(over)
        record.rover=over
        record.roversum=overpay
        absentpay=pay*8*float(absent)
        record.rabsent=absentpay
        record.rleave=leave
        record.rfoul=foul
        record.rallow=allow
        record.rname=name
        record.rpay=float(pay)
        record.rtotal=hourpay+overpay+float(allow)-float(foul)-absentpay
        record.save()
        return redirect(reverse("record-detail"))


def viewrecord(request):
    if request.method == "POST":
        showroom=request.POST['showroom']
        year=request.POST['year']
        month=request.POST['month']
        employees=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).count()
        bc=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).aggregate(a=Sum('rhoursum'))
        cd=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).aggregate(b=Sum('roversum'))
        de=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).aggregate(c=Sum('rallow'))
        ef=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).aggregate(d=Sum('rfoul'))
        fg=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).aggregate(e=Sum('rtotal'))
        gh=Record.objects.filter(Q(roffice=showroom),Q(ryear=year),Q(rmonth=month)).aggregate(f=Sum('rabsent'))
        working=bc.pop('a')
        overtime=cd.pop('b')
        allowance=de.pop('c')
        deduction=ef.pop('d')
        total=fg.pop('e')
        absent=gh.pop('f')
        two=month+"   "+showroom
        context={
            'one':'View Record',
            'two':two,
            'three':'Select Record',
            'employees':employees,
            'working':working,
            'absent':absent,
            'allowance':allowance,
            'deduction':deduction,
            'total':total,
            'overtime':overtime,
            
        }
        return render( request, 'viewrecord.html',context)
    else:
        
        context={
            'one':'View Record',
            'two':'',
            'three':'Select Record'
        }
        return render( request, 'viewrecord.html',context)
  
class EmployeeListView(ListView):
    model=EmployeeDetail
    context_object_name = 'employeeslist'
    ordering = ['nid']
    paginate_by = 5
    template_name='employeelist.html'
    
    
class EmployeeDetailView(DetailView):
    model=EmployeeDetail
    
    template_name='employeedetail.html'
    

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        employee = EmployeeDetail.object.get(pk = pk)
        employeelist=EmployeeDetail.object.all()
        context['employee'] = employee
        context['employeelist']=employeelist
        context['one']='Individual Detail'
        return context

    
def application(request):
    if request.method == "POST":
        
        date=request.POST['date']
        
        records=Application.objects.filter(date=date)
    
        context={
            'one':'Applications',
            'two':date,
            'three':'Select Date',
            'records':records,
            
        }
        return render(request, 'application.html',context)
    else:
        
        context={
            'one':'Applications',
            'two':'',
            'three':'Select Date'
        }
        return render( request, 'application.html',context)
      
def applicationdetail(request,id):
    if request.method == "POST":
        status=request.POST['status']
        empid=request.POST['empid']
        ab=Application.object.get(id=empid)
        ab.status=status
        ab.save()
        return render(request, 'application.html')
        
    record=Application.object.get(id=id)
    desc=record.desc
    empid=record.empid
    status=record.status
    reason=record.reason
    date=record.date

    context={
        'id':id,
        'date':date,
        'empid':empid,
        'status':status,
        'reason':reason,
        'desc':desc,
    }
    return render( request, 'applicationdetail.html',context)   
        
def applicationstatus(request):
    if request.method == "POST":
        status=request.POST['status']
        empid=request.POST['empid']
        ab=Application.object.get(id=empid)
        ab.status=status
        ab.save()
        
        return redirect(application)
        
        
           
        
    
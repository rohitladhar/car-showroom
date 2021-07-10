from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.db import models
from sales.models import Newcustomer,Newservice,Accessories,NewShowroom
from .forms import NewServiceForm,AddShowroomForm
import math
from django.db.models import Sum,Count
from django.db.models import Q

def saleshome(request):
    return render(request,"sales_home.html")

def logout(request):
    auth.logout(request)
    return redirect('login')

def addcustomer(request):
    return render( request, "addcustomer.html")

def customeraddition(request):
    if request.method == 'POST':
        if request.POST.get("cname"):
            cnew=Newcustomer()
            cnew.cname=request.POST.get("cname")
            if request.POST.get("cmodel"):
                cnew.cmodel=request.POST.get("cmodel")
                
                if request.POST.get("cvariant"):
                    cnew.cvarinat=request.POST.get("cvariant")
                    
                    if request.POST.get("cengine"):
                        cnew.cengine=request.POST.get("cengine")
                        if request.POST.get("cphone"):
                            cnew.cphone=request.POST.get("cphone")
                            if request.POST.get("cemail"):
                                cnew.cemail=request.POST.get("cemail")
                                if request.POST.get("cunique"):
                                    cnew.cunique=request.POST.get("cunique")
                                    if request.POST.get("cemi"):
                                        cnew.cemi=request.POST.get("cemi")
                                        if request.POST.get("cpayment"):
                                            cnew.cmode=request.POST.get("cpayment")
                                            if request.POST.get("cshow"):
                                                cnew.cshow=request.POST.get("cshow")
                                                if request.POST.get("cadvance"):
                                                    cnew.cadvance=request.POST.get("cadvance")
                                                    if request.POST.get("cloan"):
                                                        cnew.cloan=request.POST.get("cloan")
                                                        if request.POST.get("cprice"):
                                                            cnew.cprice=request.POST.get("cprice")
                                                            price=int(request.POST.get("cprice"))
                                                            if(price<1000001):
                                                                cnew.ctax=7/100*price
                                                                
                                                                cnew.save()
                                                                return HttpResponseRedirect('addcustomer')
                                                            elif(price<1500001):
                                                                cnew.ctax=6/100*price
                                                                cnew.save()
                                                                return HttpResponseRedirect('addcustomer')
                                                            else:
                                                                cnew.ctax=5/100*price
                                                                cnew.save()
                                                                return HttpResponseRedirect('addcustomer')
    else:
        return HttpResponseRedirect('sales_home')


def addservice(request):
    form=NewServiceForm()
    message={'one':'New Service Form ','two':'Ladhar Motors Sales Department'}
    context={
        'message':message,
        'form':form,
    }
    return render( request, 'newservice.html',context)

def newservice(request):
    if request.method == "POST":
        form = NewServiceForm(request.POST)
        price=form['sprice'].value()
        tax=form['stax'].value()
        acc=form['sacc'].value()
        discount=form['sdiscount'].value()
        total=0
        dis=float(discount)
        pr=float(price)
        ta=float(tax)
        length=len(acc)
        i=0
        value=0
        while(i < length): 
            value= value + float(acc[i])
            i += 1
            
        dis=dis*value
        total=dis+pr
        ta=total*ta
                
        if form.is_valid():
            service=form.save(commit=False)
            service.stotal=total
            service.stax=ta
            service.sacctotal=dis
            service.save()
            return HttpResponseRedirect('sales_home')


def addshowroom(request):
    form=AddShowroomForm()
    message={'one':'Add Showroom Form ','two':'Ladhar Motors Sales Department'}
    context={
        'message':message,
        'form':form,
    }
    return render( request, 'addshowroom.html',context)

def showroomaddition(request):
    if request.method == "POST":
        form = AddShowroomForm(request.POST)
        rent=form['srent'].value()
        main=form['smain'].value()
        units=form['sunits'].value()
        rent=float(rent)
        main=float(main)
        units=float(units)
        if (units > 10000):
            above1 = units - 10000
            above1 = above1 * 7.5
            var1 = 5000 * 5
            var2 = 2500 * 6
            var3 = 2500 * 7
            units = above1 + var1 + var2 + var3
            
        elif (units <= 10000 and units > 7500):
            above1 = units - 7500
            above1 = above1 * 7
            var1 = 2500 * 6
            var2 = 5000 * 5
            units = above1 + var1 + var2
            
        elif (units <= 7500 and units > 5001):
            above1 = units - 5000
            above1 = above1 * 6
            var1 = 5000 * 5
            units = above1 + var1
            
        elif (units <= 5000):
            units = units * 5
            
        if form.is_valid():
            service=form.save(commit=False)
            service.stotal=rent+main+units
            service.save()
            return HttpResponseRedirect('sales_home')


def carsalesview(request):
    
    if request.method == "POST":
        variant=request.POST['variant']
        model=request.POST['model']
        price=Newcustomer.objects.filter(cvarinat=variant).aggregate(a=Sum('cprice'))
        tax=Newcustomer.objects.filter(cvarinat=variant).aggregate(b=Sum('ctax'))
        advance=Newcustomer.objects.filter(cvarinat=variant).aggregate(c=Sum('cadvance'))
        loan=Newcustomer.objects.filter(cvarinat=variant).aggregate(d=Sum('cloan'))
        ab=price.pop('a')
        bc=tax.pop('b')
        cd=advance.pop('c')
        de=loan.pop('d')
        
        message={
            'one':'Total Car Sales ',
            'two':'Ladhar Motors Sales Department',
            'three':'Select Car Model'
                }
        context={
            'message':message,
            'model':model,
            'variant':variant,
            'result':Newcustomer.objects.filter(cvarinat=variant).count(),
            'price':ab,
            'tax':bc,
            'advance':cd,
            'loan':de,
        }
        return render( request, 'carsview.html',context)
    else:
        message={
            'one':'Total Car Sales ',
            'two':'Ladhar Motors Sales Department',
            'three':'Select Car Model'
                }
        context={
            'message':message,
        }
        return render( request, 'carsview.html',context)

def servicesview(request):
    if request.method == "POST":
        start=request.POST['sdate']
        end=request.POST['edate']
        d=15000
        p=10000
        diesel=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end) & Q(sdate__gte=start)).count()
        petrol=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end) & Q(sdate__gte=start)).count()
        dtax=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(a=Sum('stax'))
        ptax=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(b=Sum('stax'))
        dtotal=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(c=Sum('stotal'))
        ptotal=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(d=Sum('stotal'))
        dprice=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(e=Sum('sprice'))
        pprice=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(f=Sum('sprice'))
        dacctotal=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(g=Sum('sacctotal'))
        pacctotal=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end) & Q(sdate__gte=start)).aggregate(h=Sum('sacctotal'))
        ab=dtax.pop('a')
        bc=ptax.pop('b')
        cd=dtotal.pop('c')
        de=ptotal.pop('d')
        ef=dprice.pop('e')
        fg=pprice.pop('f')
        gh=dacctotal.pop('g')
        hi=pacctotal.pop('h')
        message={
            'one':'Total Services Amount ',
            'two':'Ladhar Motors Sales Department',
            'three':'Select Dates'
                }
        context={
            'message':message,
            'diesel':diesel,
            'petrol':petrol,
            'dtax':ab,
            'ptax':bc,
            'dtotal':cd,
            'ptotal':de,
            'dprice':ef,
            'pprice':fg,
            'dacctotal':gh,
            'pacctotal':hi,
        }
        return render( request, 'serviceview.html',context)
    else:
        message={
            'one':'Total Services Amount ',
            'two':'Ladhar Motors Sales Department',
            'three':'Select Dates'
                }
        context={
            'message':message,
        }
        return render( request, 'serviceview.html',context)

def showroomview(request):
    if request.method == "POST":
        year=request.POST['year']
        month=request.POST['month']
        rent=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(a=Sum('srent'))
        main=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(b=Sum('smain'))
        units=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(c=Sum('sunits'))
        total=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(d=Sum('stotal'))
        ab=rent.pop('a')
        bc=main.pop('b')
        cd=units.pop('c')
        de=total.pop('d')
        
        message={
            'one':'Total Showroom Expenses on Month Basis ',
            'two':'Ladhar Motors Sales Department',
            'three':'Select Dates'
                }
        context={
            'message':message,
            'year':year,
            'month':month,
            
            'rent':ab,
            'main':bc,
            'units':cd,
            'total':de,
        }
        return render( request, 'showroomview.html',context)
    else:
        message={
            'one':'Total Showroom Expenses on Month Basis ',
            'two':'Ladhar Motors Sales Department',
            'three':'Select Dates'
                }
        context={
            'message':message,
        }
        return render( request, 'showroomview.html',context)

def visual(request):
    return render( request, 'visual.html')

def visualdata(request):
    if request.method == 'POST':
        start1=request.POST['sdate1']
        end1=request.POST["edate1"]
        start2=request.POST['sdate2']
        end2=request.POST["edate2"]
        year=request.POST["year"]
        month=request.POST["month"]
        d=15000
        p=10000
        diesel1=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end1) & Q(sdate__gte=start1)).count()
        petrol1=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end1) & Q(sdate__gte=start1)).count()
        diesel2=Newservice.objects.filter(Q(sprice=d),Q(sdate__lte=end2) & Q(sdate__gte=start2)).count()
        petrol2=Newservice.objects.filter(Q(sprice=p),Q(sdate__lte=end2) & Q(sdate__gte=start2)).count()
        rent=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(a=Sum('srent'))
        main=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(b=Sum('smain'))
        units=NewShowroom.objects.filter(Q(syear=year),Q(smonth=month)).aggregate(c=Sum('sunits'))
        ab=rent.pop('a')
        bc=main.pop('b')
        cd=units.pop('c')
        creta=Newcustomer.objects.filter(cmodel="Creta").count
        tucson=Newcustomer.objects.filter(cmodel="Tucson").count
        avante=Newcustomer.objects.filter(cmodel="Avante").count
        venue=Newcustomer.objects.filter(cmodel="Venue").count
        sonata=Newcustomer.objects.filter(cmodel="Sonata").count
        verna=Newcustomer.objects.filter(cmodel="Verna").count
        context={
            'diesel1':diesel1,
            'petrol1':petrol1,
            'diesel2':diesel2,
            'petrol2':petrol2,
            'rent':ab,
            'main':bc,
            'units':cd,
            'creta':creta,
            'tucson':tucson,
            'avante':avante,
            'venue':venue,
            'verna':verna,
            'sonata':sonata,
            'month':month,
        }
        return render( request, 'charts.html',context)
    else:
        return render( request, 'charts.html')
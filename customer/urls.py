from django.urls import path
from . import views

urlpatterns=[
            #path('index',views.index,name="index"),
            path('',views.index,name="index"),
            path('bookyourcar',views.bookyourcar,name="bookyourcar"),
            path('service',views.service,name="service"),
            path('business',views.business,name="business"),
            path('addbusiness',views.addbusiness,name="addbusiness"),
            path('login',views.login,name="login"),
            path('staff',views.staff,name="staff"),
            path('userlogin',views.userlogin,name="userlogin"),
            path('bookservice',views.bookservice,name="bookservice"),
            path('servicevalue',views.servicevalue,name="servicevalue"),
            path('servicebooking',views.servicebooking,name="servicebooking"),
            path('bill',views.bill,name="bill"),
            path('customercheck',views.customercheck,name="customercheck"),
            path('servicecheck',views.servicecheck,name="servicecheck"),
            path('memberlogin',views.memberlogin,name="memberlogin"),
]

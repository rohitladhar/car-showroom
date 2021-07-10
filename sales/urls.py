from django.urls import path
from . import views

urlpatterns=[
            path('sales_home',views.saleshome,name="saleshome"),
            path('logout',views.logout,name="logout"),
            path('addcustomer',views.addcustomer,name="addcustomer"),
            path('customeraddition',views.customeraddition,name="customeraddition"),
            path('addservice',views.addservice,name="addservice"), 
            path('newservice',views.newservice,name="newservice"), 
            path('addshowroom',views.addshowroom,name="addshowroom"),
            path('showroomaddition',views.showroomaddition,name="showroomaddition"),
            path('carsalesview',views.carsalesview,name="carsalesview"),
            path('servicesview',views.servicesview,name="servicesview"),
            path('showroomview',views.showroomview,name="showroomview"),
            path('visual',views.visual,name="visual"),
            path('visualdata',views.visualdata,name="visualdata"),
]


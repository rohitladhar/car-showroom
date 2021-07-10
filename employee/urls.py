from django.urls import path
from . import views

urlpatterns=[
            path('employee_home',views.employeehome,name="employeehome"),
            path('calculator',views.calculator,name="calculator"),
            path('logout',views.logout,name="logout"),
            path('employeesalary',views.employeesalary,name="employeesalary"),
            path('recordcheck',views.recordcheck,name="recordcheck"),
            path('employeeapplication',views.employeeapplication,name="employeeapplication"),
            path('applicationstatus',views.applicationstatus,name="applicationstatus"),
            path('updateother',views.updateother,name="updateother"),
]

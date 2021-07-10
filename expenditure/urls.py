from django.urls import path
from . import views

urlpatterns=[
            path('expenditure_home',views.expenditurehome,name="expenditurehome"),
            path('logout',views.logout,name="logout"),
            path('viewrecord',views.viewrecord,name="viewrecord"),
            path('application',views.application,name="application"),
            path('addemployee',views.AddEmployeeView.as_view(),name="employee-detail"),
            path('employeelist',views.EmployeeListView.as_view(),name="employeelist"),
            path('addrecord',views.AddRecordView.as_view(),name="record-detail"),
            path('<int:pk>',views.EmployeeDetailView.as_view(),name="employeedetail"),
            path('applicationdetail/<int:id>',views.applicationdetail,name="applicationdetail"),
            path('applicationdetail/applicationstatus',views.applicationstatus,name="applicationstatus"),
]

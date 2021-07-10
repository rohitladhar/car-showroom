
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('customer.urls')),
    path('sales/',include('sales.urls')),
    path('expenditure/',include('expenditure.urls')),
    path('employee/',include('employee.urls')),
    path('admin/', admin.site.urls),
    
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
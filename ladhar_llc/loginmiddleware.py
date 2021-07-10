import re
from django.shortcuts import HttpResponseRedirect,redirect
from django.conf import settings
from django.contrib.auth import logout
EXEMPT_URLS=[re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(set,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS+=[re.compile(url) for url in settings.LOGIN_EXEMPT_URLS ]
class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request,'user')
        path=request.path_info.lstrip('/')
        

        url_is_exempt= any(url.match(path) for url in EXEMPT_URLS)

        if path=='expenditure/logout/':
            logout(request)

            
        elif path=='sales/logout/':
            logout(request)
            
        elif path=='employee/logout/':
            logout(request)
           

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_REDIRECT_URL)
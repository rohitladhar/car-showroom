from django import forms
from django.forms import ModelForm, Textarea
from .models import Business,Service

class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ('bname','bphone','bemail','boption','bmeets','bdesc')
        SELECT_OPTIONS = (
                ('', 'Select '),
                ('showroom_rental', 'Showroom Rental'), 
                ('dealership', 'Dealership'),
                ('land_sale', 'Land Sale'),
                )
        labels = {
            'bname':'Full Name',
            'bphone':'Phone',
            'bemail':'Email',
            'boption':'Options',
            'bmeets':'Meeting Slot',
            'bdesc':'Description'
        }
        widgets = {
            'bdesc': Textarea(attrs={'cols': 55, 'rows': 10}),
            'bmeets': forms.DateInput(attrs={'class':'datepicker'}),
            'boption': forms.Select(choices=SELECT_OPTIONS,attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(BusinessForm,self).__init__(*args, **kwargs)
        
        self.fields['bdesc'].required = False

class ServiceForm(forms.Form):
    name = forms.CharField()
    reg = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        self.date = kwargs.pop('date')
        self.slot = kwargs.pop('slot')
        
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['date']=forms.CharField(
            widget=forms.TextInput(attrs={'readonly':'readonly','size':self.date}),
            #initial=self.date
            )
        self.fields['slot']=forms.CharField(
            widget=forms.TextInput(attrs={'readonly':'readonly','size':self.slot}),
            #initial=self.slot
            )

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "UserName:",
        max_length = 80,
        required = True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label = "Password",
        max_length = 80,
        required = True,
    )

class CustomerBillForm(forms.Form):
    unique = forms.CharField(
        label = "Unique Number:",
        max_length = 80,
        required = True,
    )

class ServiceBillForm(forms.Form):
    unique = forms.CharField(
        label = "Unique Number:",
        max_length = 80,
        required = True,
    )

class MemberForm(forms.Form):
    username = forms.CharField(
        label = "UserName:",
        max_length = 80,
        required = True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label = "Password",
        max_length = 80,
        required = True,
    )

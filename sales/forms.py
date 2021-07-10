from django import forms
from django.forms import ModelForm, Textarea
from .models import Newservice,Accessories,NewShowroom

class NewServiceForm(forms.ModelForm):

    class Meta:
        model = Newservice
        fields = ('sunique','sname','sphone','semail','sdate','sprice','sacc','sdiscount','stax')
        PRICE_OPTIONS = (
                ('', 'Select '),
                ('10000', 'Petrol Variant'), 
                ('15000', 'Diesel Variant'),
                )
        TAX_OPTIONS = (
                ('', 'Select '),
                ('0.05', '5 percent'), 
                ('0.06', '6 percent'), 
                ('0.07', '7 percent'), 
                )
        DISCOUNT_OPTIONS = (
                ('', 'Select '),
                ('1', 'No Discount'),
                ('0.95', '5 Percent'), 
                ('0.90', '10 Percent'),
                ('0.85', '15 Percent'),
                ('0.80', '20 Percent'),
                )
        
        labels = {
            'sunique':'Bill Number:',
            'sname':'Full Name',
            'sphone':'Phone',
            'semail':'Email',
            'sdate':'Date',
            'sprice':'Service Price',
            'sacc':'Accesories',
            'sdiscount':'Discount',
            'stax':'Tax Rate'
        }
        
        widgets = {
            'sdate': forms.DateInput(attrs={'class':'datepicker'}),
            'sprice': forms.Select(choices=PRICE_OPTIONS,attrs={'class': 'form-control'}),
            'stax': forms.Select(choices=TAX_OPTIONS,attrs={'class': 'form-control'}),
            'sdiscount': forms.Select(choices=DISCOUNT_OPTIONS,attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewServiceForm, self).__init__(*args, **kwargs)
        self.fields['sacc'] = forms.MultipleChoiceField(
            choices=[(c.price, c.name) for c in Accessories.objects.all()],
            widget=forms.CheckboxSelectMultiple,
            label=("Accessories"),
            initial=[0],
            
        )
    
class AddShowroomForm(forms.ModelForm):

    class Meta:
        model = NewShowroom
        fields = ('smonth','syear','srent','sunits','smain','sshow')
        MONTH = (
                ('', 'Select '),
                ('January', 'January'), 
                ('Febuary', 'Febuary'),
                ('March', 'March'), 
                ('April', 'April'),
                ('May', 'May'), 
                ('June', 'June'),
                ('July', 'July'), 
                ('August', 'August'),
                ('September', 'September'), 
                ('October', 'October'),
                ('November', 'November'), 
                ('December', 'December'),
                )
        YEAR = (
                ('', 'Select '),
                ('2020', '2020'), 
                ('2021', '2021'), 
                ('2022', '2022'), 
                ('2023', '2023'), 
                ('2024', '2024'), 
                )
        SHOWROOM = (
                ('', 'Select '),
                ('Jalandhar', 'Jalandhar'),
                ('Ludhiana', 'Ludhiana'), 
                ('Phagwara', 'Phagwara'),
                )
        
        labels = {
            'smonth':'Month:',
            'syear':'Year',
            'srent':'Monthly Rent',
            'sunits':'Electricity Units',
            'smain':'Maintenence Amount',
            'sshow':'Showroom'
            
        }
        
        widgets = {
            'smonth': forms.Select(choices=MONTH,attrs={'class': 'form-control'}),
            'syear': forms.Select(choices=YEAR,attrs={'class': 'form-control'}),
            'sshow': forms.Select(choices=SHOWROOM,attrs={'class': 'form-control'}),
        }

from django import forms
from django.core.exceptions import ValidationError
from .models import EmployeeDetail,Record
from django.db.models import Q
class AddEmployee(forms.ModelForm):

    class Meta:
        model = EmployeeDetail
        fields = ('npost','nname','nphone','nemail','nid','noffice','ndate','npass')
        POST_LIST = (
                ('', 'Select '),
                ('Manager', 'Manager'), 
                ('Salesman', 'Salesman'),
                ('Clerk', 'Clerk'),
                ('Gate Keeper', 'Gate Keeper'),
                ('Mechanic', 'Mechanic'),
                ('Security Guard', 'Security Guard'),
                ('Pantry', 'Pantry'),
                )
        OFFICE_LIST = (
                ('', 'Select '),
                ('Jalandhar', 'Jalandhar'), 
                ('Ludhiana', 'Ludhiana'),
                ('Phagwara', 'Phagwara'),
                )
        labels = {
            'npost':'Post',
            'nid':'Unique ID',
            'nname':'Full Name',
            'nphone':'Phone',
            'nemail':'Email',
            'noffice':'Office',
            'ndate':'Joining Date',
            'npass':'Password'
        }
        widgets = {
            
            'ndate': forms.DateInput(attrs={'class':'datepicker'}),
            'npost': forms.Select(choices=POST_LIST,attrs={'class': 'form-control'}),
            'noffice': forms.Select(choices=OFFICE_LIST,attrs={'class': 'form-control'}),
        }

    def clean_nid(self):
        nid=self.cleaned_data.get('nid')
        valid_id="ladharmotors"
        
        if not valid_id in nid:
           raise forms.ValidationError('ID must include ladharmotors prefix')

        
        for instance in EmployeeDetail.objects.all():
            if instance.nid == nid:
                
                raise forms.ValidationError('Employee ID is already exist')

        return nid

    
class AddRecord(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('rid','ryear','rmonth','rhour','rover','roffice','rleave','rabsent','rfoul','rallow')
        
        OFFICE_LIST = (
                ('', 'Select '),
                ('Jalandhar', 'Jalandhar'), 
                ('Ludhiana', 'Ludhiana'),
                ('Phagwara', 'Phagwara'),
                )
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
        labels = {
            'ryear':'Year',
            'rid':'Unique ID',
            'rmonth':'Month',
            'rhour':'Working Hours',
            'rover':'Overtime Hours',
            'roffice':'Office',
            'rleave':'Leave',
            'rabsent':'Absent',
            'rfoul':'Deductions',
            'rallow':'Allowances',
        }
        widgets = {
            'rmonth': forms.Select(choices=MONTH,attrs={'class': 'form-control'}),
            'ryear': forms.Select(choices=YEAR,attrs={'class': 'form-control'}),
            'roffice': forms.Select(choices=OFFICE_LIST,attrs={'class': 'form-control'}),
        }

    def clean_rid(self):
        rid=self.cleaned_data.get('rid')

        
        if EmployeeDetail.object.filter(nid=rid).exists():
            return rid
        else:   
            raise forms.ValidationError('Employee ID is not existing')

        return rid

    def clean_rmonth(self):
        rid=self.cleaned_data.get('rid')
        month=self.cleaned_data.get('rmonth')
        year=self.cleaned_data.get('ryear')
        if Record.object.filter(Q(ryear=year),Q(rid=rid),Q(rmonth=month)).exists():
            raise forms.ValidationError('Record already exists.')

        return month

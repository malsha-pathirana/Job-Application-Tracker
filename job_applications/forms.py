from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name','job_position','job_url','applied_date','status']
        widgets = {
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            'job_position': forms.TextInput(attrs={'class':'form-control'}),
            'job_url': forms.URLInput(attrs={'class':'form-control'}),
            'applied_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }
from django import forms
from .models import Member
from django.core.validators import RegexValidator

# from .models import Person

email_regex_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    message='Enter a valid email address.'
)   

class MemberForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'email', 'phone']
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
        }

    email = forms.CharField(
        validators=[email_regex_validator],
        widget=forms.EmailInput(attrs={'placeholder': 'Enter a valid email'})
    )

    # class Meta:
    #     model = Member
    #     fields = ['firstname', 'lastname', 'email']
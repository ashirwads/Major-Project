from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import enquiry
from .models import application
from .models import payment
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	Registration_ID = forms.CharField(max_length=20, help_text='Enter your Roll no.')
	Semester = forms.CharField(max_length=20)
	Branch = forms.CharField(max_length=20)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2','Registration_ID','Semester', 'Branch']


class enquiryForm(forms.ModelForm):
	class Meta:
		model = enquiry
		fields = ['fname', 'lname', 'email', 'dob', 'gender', 'pno', 'nationality', 'course', 'highschool', 'board']

class applicationForm(forms.ModelForm):
	class Meta:
		model = application
		fields = ['fname', 'lname', 'email', 'dob', 'pno', 'gender', 'address', 'pincode', 'state', 'country', 'course']

class paymentForm(forms.ModelForm):
	class Meta:
		model = payment
		fields = ['fname', 'lname', 'email', 'dob', 'gender', 'pno', 'Registration_ID', 'Semester', 'Branch', 'course', 'cardholder', 'cardno', 'exmonth', 'exyear', 'CVV', 'amount' ]

"""from django import forms
from .models import signup
class SignupForm(forms.ModelForm):
	class Meta:
		model = signup
		fields = ['Name', 'Registration_ID', 'Email', 'Semester', 'Branch']"""


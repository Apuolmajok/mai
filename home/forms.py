from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm
from django import forms
from django.utils.safestring import mark_safe
from .models import Profile


class UserInfoForm(forms.ModelForm):
	phone=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'phone'}), required=False)
	address1=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'Address1'}), required=False)
	address2=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'Address2'}), required=False)
	city=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'city'}), required=False)
	state=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'state'}), required=False)
	zipcode=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'zipcode'}), required=False)
	country=forms.CharField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'country'}), required=False)

	class Meta:
		model=Profile
		fields=('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country',)



	





class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model=User
		fields=['new_password1','new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		
		password1_help_text = """
        <ul style="list-style-type: disc; padding-left: 20px;">
            <li>Your password can't be too similar to your other personal information.</li>
            <li>Your password must contain at least 8 characters.</li>
            <li>Your password can't be a commonly used password.</li>
            <li>Your password can't be entirely numeric.</li>
        </ul>
        """
		self.fields['new_password1'].widget.attrs['style'] = 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da;'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = mark_safe(password1_help_text)

		self.fields['new_password2'].widget.attrs['style'] = 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da;'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted";><small>Enter the same password as before, for verification.</small></span>'






class UpdateUserForm(UserChangeForm):
	password=None
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'Email Address'}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'First Name'}),required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'Last Name'}),required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', )

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['style'] = 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da;'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted";><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


		






class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'Email Address'}),required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'First Name'}),required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'style': 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da; margin-bottom: 15px;', 'placeholder': 'Last Name'}),required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['style'] = 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da;'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted";><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


		password1_help_text = """
        <ul style="list-style-type: disc; padding-left: 20px;">
            <li>Your password can't be too similar to your other personal information.</li>
            <li>Your password must contain at least 8 characters.</li>
            <li>Your password can't be a commonly used password.</li>
            <li>Your password can't be entirely numeric.</li>
        </ul>
        """
		self.fields['password1'].widget.attrs['style'] = 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da;'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = mark_safe(password1_help_text)

		self.fields['password2'].widget.attrs['style'] = 'display: block; width: 100%; padding: .375rem .75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; border: 1px solid #ced4da;'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted";><small>Enter the same password as before, for verification.</small></span>'
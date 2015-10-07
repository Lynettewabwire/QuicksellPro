from django import forms
from .models import  UserProfile,Admin, Category, Cart,Product
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
import datetime

class UserProfileForm(forms.ModelForm):

      class Meta:
            model=UserProfile
            widgets= {'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput(),
            'date_of_birth': forms.TextInput(attrs={'placeholder':'dd-mm-yyyy'})}
            fields=('__all__')
      def clean_password(self):
            password = self.cleaned_data.get('password')
            if len(password)<5:
                  raise forms.ValidationError("Password is too short")
            return password
      def clean_confirm_password(self):
            password = self.cleaned_data.get('password')
            confirm_password=self.cleaned_data.get('confirm_password')
            if confirm_password != password:
                  raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
            return confirm_password
class LoginForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['email','password',]
        widgets={
            'password':forms.PasswordInput(),
        }
    def clean_email(self):
      email=self.cleaned_data.get('email')
      users=[(user.email) for user in UserProfile.objects.filter(email=email)]
      if not email in users:
            raise forms.ValidationError("unknown email adress")
      return email
    def clean_password(self):
      user_email=self.cleaned_data.get('email')
      user_password=self.cleaned_data.get('password')
      users=UserProfile.objects.filter(email=user_email)
      for user in users:
            if user.email==user_email and user.password == user_password:
                  pass
            else:
                  raise forms.ValidationError("wrong password or email")
      return user_password


class AdminForm(forms.ModelForm):
	username =forms.CharField(max_length=30)
	password = forms.CharField(max_length=30, label ='Password', widget =forms.PasswordInput())
	class Meta:
		model =Admin
		fields ='__all__'


class CategoryForm(forms.ModelForm):
      item= forms.CharField(max_length=30, label='Item name')
      description= forms.CharField(max_length=100, label='Description')
      price = forms.IntegerField(label='Price')
      class Meta:
            model = Category
            fields='__all__'

class ProductForm(forms.ModelForm):
      stock_item=forms.CharField(label='Name', max_length=30)
      brand =forms.CharField(label='Brand', max_length=50)
      description= forms.CharField(label='Description', max_length=50)
      price= forms.DecimalField(label='Price (UGX)', max_digits=9, decimal_places=2)
      old_price= forms.DecimalField(label='Old price', max_digits=9, decimal_places=2)
      image = forms.ImageField(label='Image')
      is_active= forms.BooleanField(label='Active')
      is_bestseller =forms.BooleanField(label='is_bestseller')
      is_featured =forms.BooleanField(label='Featured')
      quantity =forms.IntegerField(label='Quantity')
      description=forms.CharField(label='Description')
      created_at =forms.DateTimeField(label='created_at')
      updated_at =forms.DateTimeField(label='updated_at')
     
      
      class Meta:
            model = Product
            fields ='__all__'
      def clean_price(self):
            if self.cleaned_data['price'] <=0:
                  raise forms.ValidationError("Price must be greater than zero")
            else:
                  return self.cleaned_data['price']


class CartForm(forms.ModelForm):
      items=forms.CharField(max_length=30, label='Item list')
      class Meta:
            model =Cart
            fields='__all__'

# data = {'first_name':'', 'last_name':'', 'email':'', 'password': '', 'confirm_password':'','dob':'', 'phoneNo':'', 'country':'', 'city':'' )

# register = RegisterUser(data)
# register.is_valid()
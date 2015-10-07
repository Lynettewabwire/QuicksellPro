from django.shortcuts import render, HttpResponse, redirect
from .models import  Category,Cart, UserProfile
from .forms import LoginForm, UserProfileForm , AdminForm, CategoryForm, CartForm
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext

#display the register form details
def register(request):

    if request.method == 'POST':
        profile_form=UserProfileForm(request.POST)

        if profile_form.is_valid():
            
            profile_form.save()

            return redirect( "/finalApp/login")
        else:
            print profile_form.errors
            print "reg failed"

       
    else:
        profile_form=UserProfileForm()
        
    	print "not valid stuff"
    	print profile_form.errors
    	

    return render(request, 'finalApp/register.html', {'profile_form':profile_form})
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
        	return redirect("/finalApp/")
            #return HttpResponse("You are now logged in")
        else:
        	print "byayanga"
    else:
        login_form = LoginForm()
        print "erooooooooooooooooo"
    return render(request, 'finalApp/login.html', {'login_form':login_form})
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def index(request):
	return render(request, 'finalApp/index.html')


def admin_login(request):
 	if request.method == 'POST':
 		adminform = LoginForm(request.POST)
 		if adminform.is_valid():
 			email = form2.cleaned_data['email']
 			password = form2.cleaned_data['password']
 			admin = Admin.objects.filter(email=email)
 			if admin:
 				for person in admin:
 					if person.email ==email and person.password==password:
 						return render(request, 'add_stock.html')
 					else:
 						raise ValidationError('incorrect details')
 			else:
 				raise ValidationError('invalid account')
 		else:
 			adminform = LoginForm()
 	else:
 		return render(request, 'finalApp/login.html', {'form2':form2})
def account_details(request):
    details = UserProfile.objects.filter()

    return render(request, 'finalApp/account.html', {'details':details})
def admin(request):
	return render(request, 'finalApp/admin_page.html')

def add_stock(request):
	if request.method == 'POST':
		categoryformform = CategoryForm(request.POST)
		
		if categoryform.is_valid():
			categoryform.save(commit=True)
			return add_stock(request)
		else:
			stockform.errors
			
	else:
		categoryform=Category()
		
	return render(request, 'finalApp/add_stock.html', {'categoryform': categoryform})

def cart(request):
	if request.method== 'POST':
		cartform= CartForm(request.POST)
		if cartform.is_valid():
			cartform.save()
		else:
			stockform.errors
	else:
		cartform=CartForm()
	return render(request, 'finalApp/cart.html', {'cartform': cartform})


# Create your views here.


# Create your views here.

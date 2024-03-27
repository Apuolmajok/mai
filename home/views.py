from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms
from django.db.models import Q


# Create your views here.

def search(request):
#Determine if they filled out the form
      if request.method=='POST':
            searched=request.POST['searched']
            #Querry the products db model
            searched=Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) |Q(price__icontains=searched))
            #Test for Null
            if not searched:
                  messages.success(request, "The product doesn't exist")
                  return render(request, "search.html", {})
            else:
                  return render(request, "search.html", {'searched':searched})
      else:
            return render(request, "search.html", {})







def update_info(request):
      if request.user.is_authenticated:
            current_user=Profile.objects.get(user__id=request.user.id)
            form=UserInfoForm(request.POST or None, instance=current_user)

            if form.is_valid():
                  form.save
                  messages.success(request, "Your Info Has Been Updated!!")
                  return redirect('Home')
            return render(request, "update_info.html", {'form':form})
      else:
            messages.success(request, "You must be logged In to Access this page!!")
            return redirect('Home')
      






def update_password(request):
       if request.user.is_authenticated:
            current_user=request.user
            #Did the user fill out the form
            if request.method=="POST":
                  form=ChangePasswordForm(current_user, request.POST)
                  #is the form valid
                  if form.is_valid():
                        form.save()
                        messages.success(request, "Your Password has been updated!!... ")
                        login(request,current_user)
                        return redirect('update_user')
                  else:
                        for error in list(form.errors.values()):
                              messages.error(request, error)
                              return redirect('update_password')
                                    
            else:
                  form=ChangePasswordForm(current_user)
                  return render(request, "update_password.html", {'form':form})
       else:
             messages.success(request, "You must be logged In to use this form")
             return redirect('Home')
             




def update_user(request):
      if request.user.is_authenticated:
            current_user=User.objects.get(id=request.user.id)
            user_form=UpdateUserForm(request.POST or None, instance=current_user)

            if user_form.is_valid():
                  user_form.save
                  login(request, current_user)
                  messages.success(request, "User Has Been Updated!!")
                  return redirect('Home')
            return render(request, "update_user.html", {'user_form':user_form})
      else:
            messages.success(request, "You must be logged In to Access this page!!")
            return redirect('Home')
     


def category(request,foo):
      #Replace hyphens with Spaces instead
      foo=foo.replace('-', ' ')
      #Grabbing the category from the url
      try:
          #Look up the Category 
          category=Category.objects.get(name=foo)
          products=Product.objects.filter(category=category)
          return render(request, 'category.html', {'products':products, 'category':category})
            
      except:
             messages.success(request, ("That Category Doesn't Exist as per now"))
             return redirect('Home')
            
      
def product(request,pk):
      product = Product.objects.get(id=pk)
      return render(request, 'product.html',{'product':product})



def Home(request):
    products = Product.objects.all()
    return render(request, 'Home.html',{'products':products})

def about(request):
        return render(request, 'about.html',{})

def zzTandC(request):
        return render(request, 'zzTandC.html',{})

def business(request):
        return render(request, 'business.html',{})

def login_user(request):
        if request.method == "POST":
               username=request.POST['username']
               password=request.POST['password']
               user = authenticate(request, username=username, password=password)
               if user is not None:
                      login(request, user)
                      messages.success(request,("You Have Been Logged In Successfully!!"))
                      return redirect('Home')
               else:
                      messages.success(request,("Incorrect password or username, please try again"))
                      return redirect('login')
                      
        else:
            return render(request, 'login.html',{})

def logout_user(request):
       logout(request)
       messages.success(request, ("You have been logged out successfully!"))
       return redirect('Home')

def register_user(request):
        form=SignUpForm()
        if request.method=="POST":
               form=SignUpForm(request.POST)
               if form.is_valid():
                      form.save()
                      username=form.cleaned_data['username']
                      password=form.cleaned_data['password1']
                      #login user
                      user=authenticate(username=username, password=password)
                      login(request, user)
                      messages.success(request, ("User created successfully, Please fill out Your User info below!!"))
                      return redirect('update_info')
               else:
                   messages.success(request, ("Oops! Registration unsuccessful, please try again"))
                   return redirect('register')
        else:
            return render(request, 'register.html',{'form':form})


#Seach  


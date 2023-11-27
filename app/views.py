# from django.shortcuts import render
# from .models import *

# # Create your views here.

# # view for Register page

# def RegisterPage(request):
#     return render(request,"app/register.html")


# # views for user registration

# def UserRegister(request):
#     if request.method =="POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']

#         #First we will validate that user already exist
#         user = User.objects.filter(Email=email)

#         if user:
#             message = "User already exist"
#             return render(request,"app/register.html",{'msg':message})
#         else:
#             if password == cpassword:
#                 newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
#                 message = "User register Successfullly"
#                 return render(request,"app/login.html",{'msg':message})
#             else:
#                 message = "Password and Confirm Password Does not match"
#                 return render(request,"app/register.html",{'msg':message})

# # Login view

# def LoginPage(request):
#     return render(request,"app/login.html")

# def LoginUser(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         #checking email id with database
#         user =User.objects.get(Email=email)

#         if user:
#             if user.Password == password:
#                 request.session['Firstname'] = user.Firstname
#                 request.session['Lastname'] = user.Lastname
#                 request.session['Email'] = user.Email
#                 return render(request,"app/home.html")
#             else:
#                 message ="password does not match"
#                 return render(request,"app/login.html",{'msg':message})
#         else:
#             message =" User does not exist"
#             return render(request,"app/register.html",{'msg':message})


# 2nd


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required



# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         if username == 'martin' and password == '12345':
#             # Set a session variable to indicate the user is logged in
#             request.session['logged'] = True
#             return redirect('home')
#         else:
#             messages.error(request, 'Incorrect username or password.')
        
#         if request.session.get('logged'):
#             return redirect('home')
        

#     return render(request, 'app/login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       if username == 'martin' and password == '12345':
           # Set a session variable to indicate the user is logged in
           request.session['logged'] = True
           return redirect('home')
       else:
           messages.error(request, 'Incorrect username or password.')

   # If the user is already logged in, redirect to the home page
   if request.session.get('logged'):
       return redirect('home')

   return render(request, 'app/login.html')


    
    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_view(request):
    # Check if the user is logged in
    if not request.session.get('logged'):
        return redirect('login')
    return render(request, 'app/home.html') 


def logout_view(request):
    # Clear the session variable to log the user out
    if request.session.get('logged'):
        del request.session['logged']
    return redirect('login')




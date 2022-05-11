# from urllib import request
from django.shortcuts import render ,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User


# Create your views here.
# Information About super user :  
# username : pihu
# gmail : pihu@gmail.com
# password : 1610
def homepage(req):
    # return HttpResponse("""<h1><b><center> This is a Home Page </center></b></h1><br> <br>
    # <a href='\about'><b> About </b> </a>""")
    context ={
        "variable1":"Piyush",
        "variable2":"Niranjan"
    }
    
    return render(req,'index.html', context)


def about(req):
    # return HttpResponse("""<h1><b><center> This is a About  Page</center></b></h1>
    # """)
    return render(req,'about.html')


def services(req):
    # return HttpResponse("""<h1><b><center> This is a Services  Page</center></b></h1>
    # """)
    return render(req,'services.html')

def contact(req):
    if req.method == 'POST' :
        name = req.POST.get('name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        desc = req.POST.get('desc')
         
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()   
        messages.success(req, "Your messages has been sent! ")  
    return render(req,'contact.html')

def signin(req):
    if req.method == "POST":
        username =  req.POST['username']
        password = req.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            fname = user.first_name
            login(req, user)
            return render(req,"index.html")
        else :
            messages.error(req," 404 request failed ")
            return redirect("home")
    return render(req,"signin.html")


def signup(req):
    if req.method=="POST":
        username = req.POST['username']
       
        email = req.POST['email']
        password = req.POST['password']
        cpassword = req.POST['password2']
        
        
        user = User.objects.create_user(username ,email ,password)
        

        user.save()
        

        messages.success(req,"your account has successfully created....")

        return redirect("signin")


    return render(req,"signup.html")

def signout(req):
    logout(req)
    messages.success(req," Logout successfully ....")
    return redirect("home")


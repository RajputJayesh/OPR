from django.shortcuts import render,redirect
from django.http import HttpResponse
from parkingapp.models import Add,Exit,Feedback
import datetime
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from parkingapp.forms import UserRegister 
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def about(request):
    if request.user.id:
        return render(request,'about.html')
    else:
        return redirect('/login')

def base(request):

    return render(request,'base.html')

def index(request):
    if request.user.id:

        return render(request,'index.html')
    else:
        return redirect('/login')
def home(request):
    if request.user.id:

     return render(request,'index.html')
    else:
        return redirect('/login')
def services(request):
    if request.user.id:

        return render(request,'services.html')
    else:
        return redirect('/login')
def pricing(request):
    if request.user.id:

        return render(request,'pricing.html')
    else:
        return redirect('/login')

def contact(request):
    if request.user.id:

        if request.method=="POST":
            na=request.POST['name']
            ma=request.POST['email']
            su=request.POST['subject']
            ms=request.POST['message']

            P=Feedback.objects.create(Name=na,E_mail=ma,sub=su,msg=ms,Created_on=datetime.datetime.now())
            P.save()
            return redirect(home)
        else:
            return render(request,'contact.html')
    else:
        return redirect('/login')

def Addvehicle(request):
    if request.user.id:
        user_id=request.user.id
        

        if request.method=="POST":
            t=request.POST['token']
            na=request.POST['name']
            ph=request.POST['phone']
            vt=request.POST.get('status')
            vn=request.POST['vehicle_number']
            pay=request.POST.get('payment')
            park=request.POST.get('v_park')
            content={}  

            if t=='':
                content['msgt']="Token Cannot be Blank"
                
            elif na=='':
                content['msgna']="Name cannot be Blank"
            elif ph=='':
                content['msgph']="Phone no cannot be Balnk"
            elif vt not in ('1','2'):
                content['msgvt']="Please Select Valid Input"
            elif vn=='':
                content['msgvn']="Vehicle no connot be Blank"
            elif pay not in ('1','2'):
                content['msgpay']="Select the Valid Input"
            else:

                P=Add.objects.create(token=t,Name=na,phone=ph,v_type=vt,v_number=vn,payment=pay,Created_on=datetime.datetime.now(),uid=user_id,v_park=park)
                P.save()
                return redirect(home)
            
            return render(request,'add_vehicle.html',content)
        
        else:
            return render(request,'add_vehicle.html')
    else:
        return redirect('/login')

def exitvehicle(request):
    if request.user.id:
        user_id=request.user.id
        
        if request.method=="POST":
            t=request.POST['token']
            na=request.POST['name']
            ph=request.POST['phone']
            vt=request.POST.get('status')
            vn=request.POST['vehicle_number']
            park=request.POST.get('v_park')
            pay=request.POST.get('payment')
            content={}

            if t=='':
                content['msgt']="Token Cannot be Blank"
                
            elif na=='':
                content['msgna']="Name cannot be Blank"
            elif ph=='':
                content['msgph']="Phone no cannot be Balnk"
            elif vt not in ('1','2'):
                content['msgvt']="Please Select Valid Input"
            elif vn=='':
                content['msgvn']="Vehicle no connot be Blank"
            elif pay not in ('1'):
                content['msgpay']="PLEASE MAKE SURE YOUR PAYMENT DONE BEFORE EXITING YOUR VEHICLE"
            else:

                P=Exit.objects.create(token=t,Name=na,phone=ph,v_type=vt,v_number=vn,payment=pay,Created_onn=datetime.datetime.now(),uid=user_id,v_park=park)
                P.save()
                return redirect(home)
            return render(request,'exit_vehicle.html',content)
        else:
            return render(request,'exit_vehicle.html')
    else:
        return redirect('/login')

def all_details(request):
    if request.user.id:

        user_id=request.user.id
        #p=Add.objects.all()
        #print(p)
        p=Add.objects.filter(uid=user_id)
        content={}
        content['data']=p
        return render(request,'all_details.html',content)
    else:
        return redirect('/login')

def exit_all_details(request):
    p=Exit.objects.all()
    r=Add.objects.all()
    #print(p)
    content={}
    content['exitdata']=p
    content['data']=r
    return render(request,'exit_all_details.html',content)

    

def catfilter(request,value):

    p=Add.objects.filter(v_type=value)
    content={}
    content['data']=p
    return render(request,'all_details.html',content)

def actfilter(request,value):

    p=Add.objects.filter(payment=value)
    content={}
    content['data']=p
    return render(request,'all_details.html',content)

def user_register(request):
    if request.method=="POST":
        regfmdata=UserRegister(request.POST)
        message={}
        if regfmdata.is_valid():
            regfmdata.save()
            message['msg']="Congratulation,Registeration Done Successfully. Please Login"
            message['x']=1
            return render(request,'msg.html',message)
        else:
            message['msg']="Failed to Register User. Plaese try again"
            message['x']=0
            return render(request,'msg.html',message)
        
    else:
        #regfm=UserCreationForm()
        regfm=UserRegister()
        content={}
        content['regfmdata']=regfm
        return render(request,'reg.html',content)

def user_login(request):
    fmlog=AuthenticationForm()
    content={}
    content['logfmdata']=fmlog
    if request.method=="POST":
        logfmdata=AuthenticationForm(request=request,data=request.POST)
        if logfmdata.is_valid():
            uname=logfmdata.cleaned_data['username']
            upass=logfmdata.cleaned_data['password']
            r=authenticate(username=uname,password=upass)
            if r is not None:
                login(request,r)
                return redirect('/')
            
        else:
            
            content['msg']="Invalid Username and Password!!!!"
            return render(request,'login.html',content)
        
    else:
        fmlog=AuthenticationForm()
        content={}
        content['logfmdata']=fmlog
        return render(request,'login.html',content)
    
   
def user_msg(request):
    return render(request,'msg.html')

def user_logout(request):
    logout(request)
    return redirect("/login")

def edit(request,rid):
    
    if request.method=="POST":
        t=request.POST['token']
        na=request.POST['name']
        ph=request.POST['phone']
        vt=request.POST.get('status')
        vn=request.POST['vehicle_number']
        park=request.POST.get('v_park')
        pay=request.POST.get('payment')
        P=Exit.objects.create(token=t,Name=na,phone=ph,v_type=vt,v_number=vn,payment=pay,Created_onn=datetime.datetime.now(),v_park=park)
        P.save()
        return redirect(home)


    else:

        p=Add.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'exit_vehicle.html',content)
    
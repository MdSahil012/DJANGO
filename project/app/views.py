from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(req):
    return render(req,'home.html') 

def Register(request):
    return render(request, "Register.html")

def Register(req):
    if req.method == 'POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        C=req.POST.get('City')
        p=req.POST.get('password')
        cp=req.POST.get('CPassword')
        ph=req.FILES.get('photo')
        a=req.FILES.get('audio')
        v=req.FILES.get('video')
        d=req.FILES.get('resume')
        q=req.POST.getlist('qualification')
        g=req.POST.get('gender')
        user = Employee.objects.filter(Email=e)
        print(user)
        if not user:
            if p == cp:
                Employee.objects.create(
                    Name=n,
                    Email=e,
                    contact=c,
                    Password=p,
                    CPassword=cp,
                    Photo=ph,
                    Audio=a,
                    Video=v,
                    Resume=d,
                    City=c,
                    Qualification=q,
                    Gender=g
                )
                return redirect  ('Login')
            else:
                msg = "Password and confirm not matched"
                userdata = {'name':n,'contact':c,'Email':e}
                return render(req,'Register.html',{'pmsg':msg,'data':userdata})
        
        else:
            msg='This email already exist'
            return render(req,'Register.html',{'msg':msg})
    
    return render(req,'Register.html')
    return redirect('register')


def Login(req):
    if req.method == 'POST':
        e=req.POST.get('email')
        p=req.POST.get('password')
        if e=='admin@gmail.com' and p=='admin':
            a_data ={
                'id':1,
                'name':'Admin',
                'email':'admin@gmail.com',
                'password':'admin',
                'image':'images/admin.jpeg'
            }
            req.session['a_data']=a_data
            return redirect('admindashboard')
            pass
        else:
            user = Employee.objects.filter(Email=e)
            if not user:
                    msg='register first'
                    return redirect('register')
            else:
                userdata=Employee.objects.get(Email=e)
            if p==userdata.Password:
                    req.session['user_id']=userdata.id
                    return redirect('userdashboard')
            else:
                    msg='email & password did not match'
                    return render(req,'Login.html',{'x':msg})
        
    return render(req, 'Login.html')


def userdashboard(req):
        if 'user_id' in req.session:
            x = req.session.get('user_id')
            userdata= Employee.objects.get(id=x)
            return render(req,'userdashboard.html',{'data':userdata})
        return redirect('Login')


def admindashboard(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        return render(req,'admindashboard.html',{'data':a_data})
    else:
        return redirect('Login')

def add_dep(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        return render(req,'admindashboard.html',{'data':a_data , 'add_dep':True})
    else:
        return redirect('Login')
    
def save_dep(req):
    if 'a_data' in req.session:
        if req.method == 'POST':
            
            dn=req.POST.get('dep_name')
            dd=req.POST.get('dep_desc')
            dh=req.POST.get('dep_head')
            dept=Department.objects.filter(dep_name=dn)
            if dept:
                messages.warning(req,'department already exist')
                a_data= req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data , 'add_dep':True})
            else:
                Department.objects.create(dep_name=dn,dep_desc=dd,dep_head=dh)
                messages.success(req,'Department created')
                a_data= req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data , 'add_dep':True})
    else:
        return redirect('Login')
    
def show_dep(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        departments = Department.objects.all()
        return render(req,'admindashboard.html',{'data':a_data , 'show_dep':True, 'departments':departments})
    else:
        return redirect('Login')

def add_emp(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        departments = Department.objects.all()
        return render(req,'admindashboard.html',{'data':a_data , 'add_emp':True,'departments':departments})
    else:
        return redirect('Login')
    

def save_emp(req):
    if 'a_data' in req.session:
        if req.method == 'POST':
        
            en=req.POST.get('name')
            ee=req.POST.get('email')    
            ec=req.POST.get('contact')
            ed=req.POST.get('dept')
            ei=req.FILES.get('image')
            eco=req.POST.get('code')
            send_mail(
                "mail from MyApp",
                f'this is information regarding your company exdential : name={en}, \n  email={ee}, \n  contact={ec}, \n dept={ed}, \n image={ei}, \n code={eco}',
                "mdsahil13304@gmail.com",
                [ee],
                fail_silently=False,
            )


            emp=Add_Employee.objects.filter(Email=ee)
            if emp:
                messages.warning(req,'Employee already exist')
                a_data = req.session.get('a_data')
                departments = Department.objects.all()
                return render(req,'admindashboard.html',{'data':a_data , 'add_emp':True,'departments':departments})
            else:
                Add_Employee.objects.create(Name=en,Email=ee,Contact=ec,Dept=ed,Image=ei,Code=eco)
                messages.success(req,'Employee created')
                a_data= req.session.get('a_data')
                departments = Department.objects.all()
                return render(req,'admindashboard.html',{'data':a_data , 'add_emp':True,'departments':departments})
    else:
        return redirect('Login')

def show_emp(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        departments = Add_Employee.objects.all()
        return render(req,'admindashboard.html',{'data':a_data , 'show_emp':True, 'departments':departments})
    else:
        return redirect('Login')
    

def Logout(req):
    if 'user_id' in req.session:
        req.session.flush()
    return render(req,'Login.html')

def about(req):
    return render(req,'about.html')



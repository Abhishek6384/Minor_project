from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Contact,Record3
from .filters import OrderFilter


from django.contrib.sessions.models import Session
# from mask.views import value
# @login_required(login_url='login')
def index(request):
    # return render(request,'index.html')
    
    if request.session.has_key('is_logged'):
        return render(request,'detect1.html')
    else:
        return render(request,'index.html')

# ide=None

def signup(request):
    form=CreateUserForm()
    
     
    if request.method =='POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user=form.cleaned_data.get('username')
            
            # print('ide : ',ide)
            messages.success(request,'Account was created for '+user)
            return redirect('login')
    context={'form':form}
    return render(request,'signup.html',context)




def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        context={user:user}
        print()
        # output=request.session
        if request.session.has_key('is_logged'):
            return render(request,'detect1.html')
        if user is not None:
            login(request,user)
            request.session['is_logged']=True
            
            return render(request,'detect1.html',context)
        else:
            messages.info(request,'Username or Password is incorrect')
            
    
    return render(request,'login.html')


def logoutUser(request):
    logout(request)

    return redirect('login')


def contact(request):
    messages.success(request,'Welcome to Contact')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<2:
            messages.error(request,'Please fill form correctly !!')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Form filled Successfully')
                
    return render(request,'contact.html')


idd=None
def save(request):
    
    if request.method=='POST':
        uid=request.POST['eid']
        result=request.POST['result']
        idd=uid
        args={'username':request.user.username,'email':request.user.email}



        print(uid)
        print(result)
        print(args['username'])
        print(args['email'])

        record=Record3(uid=uid,name=args['username'],email=args['email'],result=result)
        record.save()
        

    else:
        print('nothing')
    return render(request,'final.html',args)






def all_results(request):

    obj=Record3.objects.all()
    myfilter=OrderFilter(request.GET,queryset=obj)
    obj=myfilter.qs
    if request.session.has_key('is_logged'):
        return render(request,'results.html',{'obj':obj,'filter':myfilter})
    else:
        return redirect('login')
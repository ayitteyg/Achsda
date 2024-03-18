from django.shortcuts import render, redirect #HttpResponse, , HttpResponseRedirect
from .models import Member
from .forms import loginformC, loginform, Memberupdateform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
# Create your views here.




def info():
    info = [i for i in range (1,12)]
    context = {'info':info}
    return context


def coverpage(request):
    c = Member.objects.values_list('contact', flat=True)
    
    #print(c)
    user  = None
    form = loginformC(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #action here
            #form.save()
            contact = form.cleaned_data['contact']
           
            #authenticate and log user in at backend
            #print(contact)
            user = contact #'0549053295'
            #print(request.user)
            if user in c:
                #u = Member.objects.filter(contact=user)[0]
                #context = {'usr':u}
                return redirect ('homepage')

            else:
                messages.info(request, 'contact is not registered')
                return render (request, 'coverpage.html', {'form':form})
    else:
        form = loginformC()
    return render (request, 'coverpage.html', {'form':form})



def officerslogin(request):
    user  = None
    form = loginform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #action here
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #authenticate and log user in at backend
            user = authenticate(username=username, password=password)
            #print(request.user)
            if user is not None:
                user_login(request, user)
                #print(request.user)
                return redirect ('officerspage')

            else:
                messages.info(request, 'authentication failed')
                return render (request, 'homepage.html', {'form':form})
    else:
        form = loginform()
    return render (request, 'officerslogin.html', {'form':form})



def homepage(request):
    c = info()
    return render (request, 'homepage.html', c)


def officerspage(request):
    c = info()
    return render (request, 'adminpage.html', c)


def memberpage(request):
    lst = Member.objects.all()
    T = len(lst)
    A = len([i for i in Member.objects.filter(cstatus="Active")])
    NA = len([i for i in Member.objects.filter(cstatus="NonActive")])
    M = len([i for i in Member.objects.filter(gndr="M")])
    F = len([i for i in Member.objects.filter(gndr="F")])
    Mr = len([i for i in Member.objects.filter(mstatus="married")])
    S = len([i for i in Member.objects.filter(mstatus="single")])
    

    #print(len(lst))
    #print(M)
    #print(S)
    
    c  = info()
    context = {'lst':lst, 'T':T, 'A':A, 'NA':NA, 'M':M, 'F':F, 'Mr':Mr, 'S':S}
    context.update(c)
   
    return render (request, 'memberpage.html', context)





from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.

def homepage(request):
    return render (request, 'homepage.html')


def memberpage(request):
    lst = Member.objects.all()
    M = len([i for i in Member.objects.filter(mstatus="married")])
    S = len([i for i in Member.objects.filter(mstatus="single")])

    #print(len(lst))
    #print(M)
    #print(S)

    context = {'lst':lst, 'T':len(lst), 'M':M, 'S':S}
   
    return render (request, 'memberpage.html', context)
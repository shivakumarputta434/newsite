from django.http import HttpResponse
from django.shortcuts import render
def how(request):
        return render(request,"welcome.html")
def wel(request):
    return HttpResponse("welcome")

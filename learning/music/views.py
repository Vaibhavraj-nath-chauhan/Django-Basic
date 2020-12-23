from django.shortcuts import render
from django.http import HttpResponse

#Vaibhavraj Nath Chauhan

def student(request):
    return HttpResponse("Its Working")

def check(request):
    return HttpResponse("<h1>My Second Function Checking</h1>")

def my_work(request):
    return HttpResponse('<h1 style="color:yellow">Home Work</h1>')

def no_work(request):
    return HttpResponse("<h1>Again Checking</h1>")

def zero_work(request):
    return HttpResponse("<center><h1 style='color:pink'>Checking One more time</h1></center>")

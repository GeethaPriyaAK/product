import datetime
from django.shortcuts import render

# Create your views here.
def hello(request):
    today = datetime.datetime.now().date(),

    return render(request,'hello.html',{"todayvar":today})



def hello1(request):
    today = datetime.datetime.now().date(),
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})
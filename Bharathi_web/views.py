from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    return render(request, 'Bharathi_web/index.html')

def base(request):
    return render(request, 'Bharathi_web/base.html')

def index1(request):
    message = "Hi "
    name=["Surya","prakash","srini"]
    time = datetime.datetime.now()
    hour = int(time.strftime('%H'))
    if hour<12:
        message+="Good Moring"
    else:
        message+="Good Evening"
    dic = {"name":name,'time':time,'message':message}
    return render(request, 'Bharathi_web/index1.html',context=dic,)

def chapter1(request):
    return render(request, 'Bharathi_web/chapter1.html')

def about(request):
    return render(request, 'Bharathi_web/about.html')
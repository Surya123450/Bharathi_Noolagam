from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Bharathi_web/index.html')

def index1(request):
    return render(request, 'Bharathi_web/index1.html')

def chapter1(request):
    return render(request, 'Bharathi_web/chapter1.html')

def about(request):
    return render(request, 'Bharathi_web/about.html')
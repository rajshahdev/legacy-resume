from django.shortcuts import render

# Create your views here.

def service(request):
    return render(request,'serve/services.html')
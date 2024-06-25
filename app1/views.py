from django.shortcuts import render

# Create your views here.
def crazy(request):
    return render(request,'crazy.html')
def majamaja(request):
    return render(request,'majamaja.html')
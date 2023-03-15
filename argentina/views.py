from django.shortcuts import render

# Create your views here.
def messy(request):
    return render(request,'messy.html')
def ronaldo(request):
    return render(request,'ronaldo.html')
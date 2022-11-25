from django.shortcuts import render

# Create your views here.
def third(request):
    d={'a':25,'b':45,'c':46}
    return render(request,'third.html',d)

def forth (request):
    d={'name':'jagadeesh','age':22}
    return render(request,'forth.html',d)
from django.shortcuts import render

# Create your views here.
def first(request):
    d={'a':7,'b':25,}
    return render(request,'one.html',d)

def second(request):
    d={'a':5,'b':25,'c':92}
    return render(request,'second.html',d)
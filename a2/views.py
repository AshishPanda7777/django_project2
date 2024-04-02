from django.shortcuts import render
from django.http import HttpResponse

def csk(request):
    return render(request,'ipl.html')

# Create your views here.

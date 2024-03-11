from django.shortcuts import render
from django.http import HttpResponse
# from .models import 

# Create your views here.
def Register(request):
    return render(request,'Register.html',{'Register':'Register',
                                           })
    
def Login(request):
    return render(request,'Login.html',{'Login':'Login',
                                           })
    
def Home(request):
    return render(request,'Home.html',{'Home':'Home',
                                           })
    
def Profile(request):
    return render(request,'Profile.html',{'Profile':'Profile',
                                           })
    
def Chat(request):
    return render(request,'Chat.html',{'Chat':'Chat',
                                           })
    
def profileCreation(request):
    return render(request,'profileCreation.html',{'profileCreation':'profileCreation',
                                           })
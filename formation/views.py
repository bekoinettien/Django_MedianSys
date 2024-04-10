from django.shortcuts import render
from formation.forms import SignupForm
def home(resquest):
    return render(resquest,'home.html')
    
def propos(resquest):
    return render(resquest,'propos.html')

# Create your views here.
def signup(resquest):
    form = SignupForm()
    return render(resquest,'compte/signup.html',{"form":form})
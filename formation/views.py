from django.shortcuts import render
def home(resquest):
    return render(resquest,'home.html')

def propos(resquest):
    return render(resquest,'propos.html')

# Create your views here.

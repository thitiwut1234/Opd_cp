from django.http import request
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("<h2>Home</h2>")
    return render(request , 'index.html' )
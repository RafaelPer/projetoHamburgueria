from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepageShow(request):
    return render(request, 'homepage/index.html')
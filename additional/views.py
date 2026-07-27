from django.shortcuts import render
from .models import *
# Create your views here.
def Hello(request):
    context={
        "market":uzum_market.objects.all(),
        "kompyuter":kompyuter.objects.all(),
    }
    return render(request,'hello.html',context)

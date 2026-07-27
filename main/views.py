from django.shortcuts import render
from additional.models import *
# Create your views here.
def Index(request):
    context={
         "uzum":uzum_market.objects.all(),
          "dacha":dacha.objects.all()

    }
    return render(request,'index.html',context)

def Home(request):
     context={
          "dacha":dacha.objects.all(),
          "uzum":uzum_market.objects.all()
     }
     
        
     return render(request,'home.html',context)
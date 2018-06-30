from django.shortcuts import render
#from .forms import UserForm

def home(request):
   return render(request, 'index.html')


def area_logada(request):
   return render(request, 'AreaLogada.html')


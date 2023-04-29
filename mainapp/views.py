from django.shortcuts import render
from django.http import HttpResponse
import sys
import joblib 

# Create your views here.
def index(request):
     context = {}
     return render(request, 'mainapp/home.html', context)


def input(request):
     context = {}
     return render(request, 'mainapp/INPUT.html', context)


def RESULTS(request):
    

     cls = joblib.load('finalized_model.sav')
     lis = []
     lis.append(request.POST.get('n_ratio'))
     lis.append(request.POST.get('p_ratio'))
     lis.append(request.POST.get('k_ratio'))
     lis.append(request.POST.get('temperature'))
     lis.append(request.POST.get('humidity'))
     lis.append(request.POST.get('ph'))
     lis.append(request.POST.get('rainfall'))
     print(lis)
     ans = cls.predict([lis])
     if(ans==0):
          answer = 'Apple'
     elif(ans==1):
          answer = 'Banana'
     elif(ans==2):
          answer = 'Blackgram'
     elif(ans==3):
          answer = 'Chickpea'
     elif(ans==4):
          answer = 'Coconut'
     elif(ans==5):
          answer = 'Coffee'
     elif(ans==6):
          answer = 'Cotton'
     elif(ans==7):
          answer = 'Grapes'
     elif(ans==8):
          answer = 'Jute'
     elif(ans==9):
          answer = 'Lentil'
     elif(ans==10):
          answer = 'Lentil'
     elif(ans==11):
          answers = 'Maize'
     elif(ans==12):
          answer = 'Mango'
     elif(ans==13):
          answer = 'mothbeans'
     elif(ans==14):
          answer = 'Mungbean'
     elif(ans==15):
          answer = 'Muskbean'
     elif(ans==16):
          answer = 'Orange'
     elif(ans==17):
          answer = 'Papaya'
     elif(ans==18):
          answer = 'Pigeonpeas'
     elif(ans==19):
          answer = 'Pomegranate'
     elif(ans==20):
          answer = 'rice'
     elif(ans==21):
          answer = 'watermelon'
     else:
          answer = "ERROR"
     context = {}


     return render(request, 'mainapp/RESULTS.html', {'answer':answer})
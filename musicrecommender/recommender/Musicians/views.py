from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Song
from django.views import View
def home(request):
    return render(request, 'Musicians/home.html')


def m1(request):
    return render(request, 'Musicians/m1.html')


def m2(request):
    return render(request, 'Musicians/m2.html')


def m3(request):
    return render(request, 'Musicians/m3.html')


def m4(request):
    return render(request, 'Musicians/m4.html')


def viewsongs(request):
    return render(request, 'Musicians/view.html', {'Slist': Song.objects.all()})



import pandas as pd


class ml(View):
    def post(self, request):
        print('result')
        model = pd.read_pickle(r'C:\Users\jithe\Downloads\coursera-courses\ml project\new_model1.pickle')
        genre=request.POST.get('genre')
        listened=request.POST.get('listened')
        if genre == 'Classics':
            genre=0
        elif genre == 'Devotional':
            genre=1
        elif genre =='Comedy':
            genre=3
        result = model.predict([[genre, listened]])
        print(result)
        return render(request, 'Musicians/mlresult.html',{'result':result},)
    def get(self, request):
        return render(request, 'Musicians/ml.html')
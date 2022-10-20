
from django.shortcuts import render ,redirect 
from multiprocessing import context
from unittest import result
import random 	


def index(request):
    return render(request,'index.html')

def process(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    if request.POST['action'] == 'Farm':
        random_number = random.randint(10, 21)
        request.session['gold'] += random_number
    elif request.POST['action'] == 'Cave':
        random_number = random.randint(10, 21)
        request.session['gold']  += random_number
    elif request.POST['action'] == 'House':
        random_number = random.randint(-50, 101)
        request.session['gold']  += random_number
    elif request.POST['action'] == 'Quest':
         random_number = random.randint(0,51)
         request.session['gold']  += random_number
    return redirect('/')


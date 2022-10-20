
import email
from email.message import Message
from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.forms import PasswordInput
from django.shortcuts import render ,redirect
from django.contrib import messages
import bcrypt
from login.models import User

def main_page(request):
    return render(request,"index.html")


def registration(request):
    form =request.POST
    errors=User.objects.basic_validator(form)
    if len(errors)>0:
        for key , val in errors.items():
            messages.error(request,val)
        return redirect('/')
    user = User.objects.create(first_name=form['first_name'],last_name=form['last_name']
    ,email=form['email'],password=bcrypt.hashpw(form['password'].encode(),bcrypt.gensalt()).decode())
    request.session["user_id"]= user.id
    return redirect('/books')

def login(request):
    form =request.POST
    try:
        user=User.objects.get(email=form['email'])
    except:
        messages.error(request,'check youre email and password!')
        return redirect('/')
    if bcrypt.checkpw(form['password'].encode(),user.password.encode()):
        request.session['user_id']= user.id
        return redirect('/books')
    messages.error(request,'check youre email and password!')
    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/') 





    

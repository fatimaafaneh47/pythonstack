from django.shortcuts import render ,redirect
from django.forms import PasswordInput
from django.shortcuts import render ,redirect
import bcrypt
from login.models import User
from the_wall.models import*


def success(request):
    if "user_id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])

    context={
        'user': user,
        'messages':Message.objects.all(),
        'comment':Comment.objects.all(),
    }
    return render (request,"success.html",context)


def message(request):
    user=User.objects.get(id=request.session['user_id'])
    message=request.POST['message']
    m1=Message(message=message,user=user)
    m1.save()
    return redirect('/wall')

def comment(request,id):
    user=User.objects.get(id=request.session['user_id'])
    comment=request.POST['comment']
    m2 = Message.objects.get(id=int(id))
    c1=Comment(comment=comment,user=user,message=m2)
    c1.save()
    return redirect('/wall')


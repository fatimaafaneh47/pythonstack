
from multiprocessing import context
from django.shortcuts import render ,redirect
from .models import Users

def index(request):
    context = {
        "all_users":
    Users.objects.all()
    }
    return render(request,"index.html",context)

# request.POST is dictionary: has keys (the name attribute in the form)
# it has values also, which are the data inserted by the users
def results(request):
    Users.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],email_address=request.POST['email'],age=request.POST['age'])
    return redirect("/")


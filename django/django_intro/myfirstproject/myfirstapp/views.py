from django.shortcuts import render ,HttpResponse,redirect

 
def root(request):
    return redirect('blogs/')

def index(request):
    return HttpResponse("response from index method from root route")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request,my_val):
    return HttpResponse("placeholder to display blog number:" + str(my_val))

def edit(request,my_val):
    return HttpResponse("placeholder to edit blog "+ str(my_val))

def destroy(request,my_val):
    return redirect('/blogs')

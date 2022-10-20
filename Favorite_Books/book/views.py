
from multiprocessing import context
from turtle import title
from django.shortcuts import render,redirect
import book
from book.models import Book
from login.models import User
from django.contrib import messages
def success(request):
    if "user_id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context={
        'user': user, 
        "books":Book.objects.all(),
    }
    return render (request,"success.html",context)

def add(request):
    form =request.POST
    errors=Book.objects.basic_validator(form)
    if len(errors)>0:
        for key , val in errors.items():
            messages.error(request,val)
        return redirect('/books')
    logged_user = User.objects.get(id = request.session['user_id'])
    
    this_book = Book.objects.create(Title=form["title"],desc=form["description"],user = logged_user)
   
    logged_user.books.add(this_book)		
    return redirect('/books')


def single_book(request,book_id):
    context={
        'book':Book.objects.get(id=book_id),
        'this_user': User.objects.get(id = request.session['user_id']),
        'user_liked_one_book':Book.objects.get(id=book_id).users.all(),      
    }
    return render(request,'after_link.html',context)
        
def show(request,book_id):
    form =request.POST
    this_user= User.objects.get(id = request.session['user_id']),
    Book.objects.get(id=form["book_id"],Title=form('title'),desc=form["description"],user = this_user)
    return redirect(f"/books/{book_id}")

def show_user(request,book_id):
    book= Book.objects.get(id=book_id)
    this_user = User.objects.get(id= request.POST["user_id"])
    book.users.add(this_user)
    

    return redirect(f"/books/{book_id}")

def delete(request,book_id):
    delete_book=Book.objects.get(id=book_id)
    delete_book.delete()
    return redirect("/books")


def update(request,book_id):
    book = Book.objects.get(id=book_id)
    form=request.POST
    book.Title=form['title']
    book.desc=form['description']
    book.save()
    return redirect(f'/books/{book_id}')

def favorites(request,book_id):
    book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id= request.POST["user_id"])
    book.users.add(this_user)
    return redirect(f'/books/{book_id}')

def add_favorites(request,book_id):
    logged_user = User.objects.get(id = request.session['user_id'])
    
    this_book = Book.objects.get(id = book_id)
   
    logged_user.books.add(this_book)		
    return redirect(f'/books/{book_id}')

def delete_favorites(request,book_id):
    logged_user = User.objects.get(id = request.session['user_id'])
    
    this_book = Book.objects.get(id = book_id)
    logged_user.books.remove(this_book)		
    return redirect(f'/books/{book_id}')
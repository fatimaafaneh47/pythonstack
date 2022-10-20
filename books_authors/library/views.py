
from turtle import title
from django.shortcuts import render ,redirect
from .models import Author, Book 

def index(request):
    context ={
        "books":Book.objects.all()
    }
    return render(request,"index.html",context)

def add_book(request):
    form =request.POST
    Book.objects.create(
    title=form["title"],
    desc=form["description"],
    )
    return redirect('/')

def authors(request):
    context={
        "authors":Author.objects.all()
    }
    return render(request,"authors.html",context)


def add_author(request):
    form=request.POST
    Author.objects.create(
        first_name=form["firstname"],
        last_name=form['lastname'],
        notes=form["notes"],
    )
    return redirect('/authors')

def single_book(request,book_id):
    context={
        "book": Book.objects.get(id=book_id),
        "authors":Author.objects.all()
    }
    return render(request,"book_details.html",context)

def add_author_to_book(request,book_id):
    this_book= Book.objects.get(id=book_id)
    author = Author.objects.get(id= request.POST["author_id"])
    this_book.authors.add(author)
    return redirect(f"/books/{book_id}")

def author_details(request,author_id):
    context={
        "author": Author.objects.get(id=author_id),
        "books":Book.objects.all()
    }
    return render(request,"author_details.html",context)

def add_book_to_author(request,author_id):
    this_author= Author.objects.get(id=author_id),
    book=Book.objects.get(id=request.POST["book_id"])
    this_author.books.add(book)
    return redirect(f"/authors/{author_id}")



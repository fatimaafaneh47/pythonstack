from multiprocessing import context
from django.shortcuts import render ,redirect
from django.contrib import messages

from.models import Show

def all_shows(request):
    context ={
        "shows":Show.objects.all()
    }
    return render(request,"All_Shows.html",context)
 
def new_show(request):
    return render(request,"new_show.html")

def tv_show(request,show_id):
    context={
        "show":Show.objects.get(id=show_id)
    }
    return render(request,"tv_show.html",context)

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        
        for error in errors.values():
            messages.error(request, error)
        return redirect("/shows/new")
       
    form =request.POST
    created_show=Show.objects.create(
        title=form["title"],
        network=form['network'],
        Realease_Date=form['realease_date'],
        desc=form["description"],
    )
    return redirect(f"/shows/{created_show.id}")


def delete(request,show_id):
    delete_show=Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect("/shows")

def edit_page(request,show_id):
    show=Show.objects.get(id=show_id)
    show.Realease_Date=show.Realease_Date.strftime("%Y-%m-%d")
    context={
        "show":show
    }
    return render(request,"edit_show.html",context)

def update(request,show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        
        for error in errors.values():
            messages.error(request, error)
        return redirect(f'/shows/{show_id}/edit')
    show = Show.objects.get(id=show_id)
    post=request.POST
    show.title=post['title']
    show.network=post['network']
    show.Realease_Date=post['release_date']
    show.desc=post['description']
    show.save()
    return redirect(f'/shows/{show_id}')


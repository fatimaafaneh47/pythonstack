
from django.shortcuts import render
def root(request):
    return render(request, "index.html")

def display(request):
    print("Here")
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']

    context = {
    'name': name,
    'location': location,
    'language': language,
    'comment': comment,
    }
    return render(request, "results.html",context)
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Cat

# Create your views here.
def home(request):
    #include an .html file extension - unlike when rendering EJS templates 
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'main_app/cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, "main_app/cats/detail.html", {"cat": cat})


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/' not the preferred way to do this
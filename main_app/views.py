from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Cat
from .forms import FeedingForm

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
    #instantiate Feeding Form to be rendered
    feeding_form = FeedingForm()
    return render(request, "main_app/cats/detail.html", {"cat": cat, 'feeding_form': feeding_form})

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/' not the preferred way to do this

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

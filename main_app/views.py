from django.shortcuts import render

# views.py

# Add this cats list below the imports
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Tsuki', 'breed': 'tuxedo', 'description': 'furry little demon, but also gentle, loving, best cat around', 'age': 2},
]


# Create your views here.
def home(request):
    #include an .html file extension - unlike when rendering EJS templates 
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def cats_index(request):
    return render(request, 'main_app/cats/index.html', {'cats': cats})
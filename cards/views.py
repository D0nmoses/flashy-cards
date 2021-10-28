from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'all-cards/home.html')

def about(request):
    return render(request, 'all-cards/about.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import get_object_or_404
# Create your views here.

# def home(request):
#     return HttpResponse('<h1>this is home</h1>')

searchTerm = None

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})

def about(request):
    return HttpResponse('<h1>this is about</h1>')

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all() 
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})


def signup(request):
    email = request.GET.get('email')
    
    if request.method == 'POST':
        pass

    return render(
        request=request, 
        template_name='email.html', 
        context = {'email':email}
    )
 
from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse


TMDB_API_KEY = "b09d9bb6f2d716660b3b279d4ecf66d3"
def search(request):
    print(request)
    query_movie = request.GET.get('q-movie')
    query_tv = request.GET.get('q-tv')
    type = "movie_details"
    #If the query is not empty
    if(query_movie):
        #Get the results from the API
        data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={ TMDB_API_KEY }&page=1&query={query_movie}")
        
        
    elif(query_tv):
        type = "tv_details"
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={ TMDB_API_KEY }&page=1&query={query_tv}")
    
    else:
        return HttpResponse("Please enter a search query")
    
    #Render the Template
    return render(request, 'Home/results.html', {
        "data" : data.json,
        "type" : type
    })

def index_movie(request):
    return render(request, 'Home/index_movie.html')


def index_tv(request):
    return render(request, 'Home/index_tv.html')

def view_tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{ tv_id }?api_key={ TMDB_API_KEY }&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{ tv_id }/recommendations?api_key={ TMDB_API_KEY }&language=en-US")
    return render(request, 'Home/tv_details.html',{
        "data" : data.json(),
        "recommendations": recommendations.json(),
        "type" : "tv_details",
    })
    
def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{ movie_id }?api_key={ TMDB_API_KEY }&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{ movie_id }/recommendations?api_key={ TMDB_API_KEY }&language=en-US")
    return render(request, 'Home/movie_details.html',{
        "data" : data.json(),
        "recommendations" : recommendations.json(),
        "type" : "movie_details",
    })
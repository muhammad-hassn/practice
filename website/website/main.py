# I create this file -----------> muhammad hassan

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')
    # return HttpResponse('''<h1>Hy Muhammad Hassan</h1> 
    #                     <button><a href="http://127.0.0.1:8000/about"> NEXT </a></button>
    #                     ''')

def removepunc(request):
    # GET THE TEXT 
    djText = request.GET.get('text','default')
    print(djText)
    # ANALIZED THE TEXT
    return HttpResponse("removepunc")

def aboutremover(request):
    return HttpResponse("about remover")

def aboutadd(request):
    return HttpResponse("hello")

def aboutsub(request):
    return HttpResponse("hy i ma muhammad hassan")

def about(request):
    return HttpResponse("hy Im muhammad hassan atique")

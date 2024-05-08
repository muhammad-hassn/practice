# I create this file -----------> muhammad hassan

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request , 'index.html')
    # return HttpResponse('''<h1>Hy Muhammad Hassan</h1> 
    #                     <button><a href="http://127.0.0.1:8000/about"> NEXT </a></button>
    #                     ''')

def ANALYZED(request):
    # GET THE TEXT 
    
    djText = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'OFF')
    print(removepunc)
    print(djText)
    punctuation = '''+_*&^%$#@!{}-()[]?><"\':;/'''
    analyzed1 = ""
    if removepunc == "on":
        for char in djText:
            if char  not in punctuation:
                analyzed1 = analyzed1  +  char
    else:
        return HttpResponse("ERROR")

    params = {'purpose': 'Remove Punctuation' , 'Analyzed_text': analyzed1}
    return render(request, "analyzed.html", params)

# def aboutremover(request):
#     return HttpResponse("about remover")

# def aboutadd(request):
#     return HttpResponse("hello")

# def aboutsub(request):
#     return HttpResponse("hy i ma muhammad hassan")

# def about(request):
#     return HttpResponse("hy Im muhammad hassan atique")

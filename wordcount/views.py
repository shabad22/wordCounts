from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def count(request):
    data = request.GET['fulltext']
    l = data.split()
    length = len(l)
    worddic = {}
    for word in l:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    return render(request, 'count.html', {'text':data,'words':length,'worddict':worddic.items()})
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
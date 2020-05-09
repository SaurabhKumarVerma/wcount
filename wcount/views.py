from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    print(type(wordlist))



    worddictnory = { word : wordlist[word] for word in range(0, len(wordlist) ) }
    print(worddictnory)


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictnory':worddictnory.items()}) #fulltext in syting in dictnory will pass in count.html

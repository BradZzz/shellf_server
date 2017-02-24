from django.shortcuts import render
from main.lib.parse import parsedBooks
from django.http import JsonResponse

#TODO:
#Add an endpoint for listing books
#Add an endpoint for comparing two books to each other
#   Word differences
#   Sentiment differences
#Add an endpoint for comparing all books to each other

books = parsedBooks()

# Create your views here.
def list(request):
    return JsonResponse({'data':books.list()})

# Return stored polarity / sentiment
def analyze(request, book):
    return JsonResponse({'data':books.analyze(int(book))})

# Compare the frequency of top words
def compare(request, book1, book2, pos):
    return JsonResponse({'data':books.compare(int(book1), int(book2), int(pos))})

# Return the sentiment and word similarity matrices
def similarity(request):
    return JsonResponse({'data':books.similarity()})

# Return the similarity matrix condensed with PCA
def condense(request):
    return JsonResponse({'data':books.condense()})
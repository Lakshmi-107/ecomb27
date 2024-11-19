# from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.

# def home(request):
#     context = {
#         "first_name": "Lakshmi",
#         "second_name": "Jeni",
#     }
#     return render(request, 'home.html', context)
#
#
# def demo(request):
#     number = {
#         'num': -10,
#     }
#     return render(request, 'demo.html', number)


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def books(request):
    books = [
        {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": 1960},
        {"id": 2, "title": "Harry Potter", "author": "J.K. Rowling", "publication_year": 2000},
        {"id": 3, "title": "Life of Pi", "author": "Yann Martel", "publication_year": 2001},
        {"id": 4, "title": "The Help", "author": "Kathryn Stockett", "publication_year": 2009},
        {"id": 5, "title": "Cloud Cuckoo Land", "author": "Anthony Doerr", "publication_year": 2021},

    ]

    context = {
        'books': books
    }

    return render(request, 'books.html', context)



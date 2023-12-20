from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

import xml_rpc
from .forms import SearchBookForm
from .models import Book


def home(request):
    return redirect('odoo_config:index')

class BookView(ListView):
    model = Book
    template_name = "book_rating/books.html"
    context_object_name = "book"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookForm'] = SearchBookForm
        return context


def _read_info():
    try:
        with open(settings.BASE_DIR / '.env', 'r') as f:
            content = f.read()
            login, username = content.strip().split(',')
            return login, username
    except FileNotFoundError:
        # Gérer le cas où le fichier .env n'existe pas encore
        return None, None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier .env: {e}")
        return None, None


def search(request):
    form = SearchBookForm(request.POST)
    context = {}
    if form.is_valid():
        title = form.cleaned_data['title']
        try:
            login, username = _read_info()
            if login is not None and username is not None:
                uid = xml_rpc.connect(username, login)
                if xml_rpc.check_access_rights(uid, login):
                    books = sortBooksByLikesAndName(xml_rpc.search_book_by_name(uid, login, title))
                    context['books'] = books
                    return render(request, 'book_rating/book.html', context)
                else:
                    messages.error(request, "Please connect to Odoo !")
        except ConnectionError:
            messages.error(request, "The 0doo server is not started!")
    return HttpResponseRedirect(reverse('book_rating:books'))


def like(request):
    book_id = request.POST.get('book_id')
    book_title = request.POST.get('book_title')
    context = {}
    try:
        login, username = _read_info()
        if login is not None and username is not None:
            uid = xml_rpc.connect(username, login)
            if xml_rpc.check_access_rights(uid, login):
                xml_rpc.like(uid, login, book_id)
                books = sortBooksByLikesAndName(xml_rpc.search_book_by_name(uid, login, book_title))
                context['books'] = books
                messages.success(request, "Like added !")
                return render(request, 'book_rating/book.html', context)
            else:
                messages.error(request, "Request failed !")
    except ConnectionError:
        messages.error(request, "The 0doo server is not started!")
    return HttpResponseRedirect(reverse('book_rating:books'))


def sortBooksByLikesAndName(books):
    return sorted(books, key=lambda book: (book['likes_count'], book['name']), reverse=True)
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import User, Book , UserBook
from .forms import UserForm, BookForm, UserBookForm


class HomeView(View):
    def get(self, request):
        return render(
            request,
            "home.html"
        )

class BookView(View):
    def get(self, request):
        search = request.GET.get("search", "").strip()

        books = Book.objects.all()

        if search:
            books = books.filter(
                title__icontains=search
            ) | books.filter(
                author__icontains=search
            )

        return render(
            request,
            "book/book_list.html",
            {
                "books": books,
                "search": search,
            }
        )
class DetailBookView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(
            request,
            "book/detail_book.html",
            {
                "book": book
            }
        )
class CreateBookView(View):
    def get(self, request):
        form = BookForm()

        return render(
            request,
            "book/create_book.html",
            {
                "form": form
            }
        )

    def post(self, request):
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("books")

        return render(
            request,
            "book/create_books.html",
            {
                "form": form
            }
        )




class UserView(View):
    def get(self, request):
        search = request.GET.get("search", "").strip()

        users = User.objects.all()

        if search:
            users = users.filter(
                first_name__icontains=search
            ) | users.filter(
                last_name__icontains=search
            )

        return render(
            request,
            "user/user_list.html",
            {
                "users": users,
                "search": search,
            }
        )
class UserDetailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(
            request,
            "user/detail_user.html",
            {
                "user": user
            }
        )

class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(
            request,
            "user/create_user.html",
            {
                "form": form
            }
        )
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
        return render(
            request,
            "user/create_user.html",
            {
                "form": form
            }
        )





class UserBookView(View):
    def get(self, request):
        search = request.GET.get("search", "")

        if search:
            userbooks = UserBook.objects.filter(
                Q(book__title__icontains=search) |
                Q(book__author__icontains=search)
            )
        else:
            userbooks = UserBook.objects.all()

        return render(
            request,
            "userbook/userbook_list.html",
            {
                "userbooks": userbooks,
                "search": search,
            }
        )

class DetailUserBookView(View):
    def get(self, request, pk):
        userbook = UserBook.objects.get(pk=pk)
        return render(
            request,
            "userbook/detail_userbook.html",
            {
                "userbook": userbook
            }
        )
class CreateUserBookView(View):
    def get(self, request):
        form = UserBookForm()
        return render(
            request,
            "userbook/create_userbook.html",
            {
                "form": form
            }
        )
    def post(self, request):
        form = UserBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userbooks")
        return render(
            request,
            "userbook/create_userbook.html",
            {
                "form": form
            }
        )
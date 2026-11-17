from django import forms
from .models import User, Book, UserBook

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'role', 'age')
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'count', 'description')
class UserBookForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ('user', 'book')

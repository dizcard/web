from django.urls import path
from .views import (
    HomeView,
    UserView ,UserDetailView,CreateUserView,
    BookView ,DetailBookView,CreateBookView,
    UserBookView, DetailUserBookView,CreateUserBookView
)

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('book/', BookView.as_view(), name='books'),
    path('books/<int:pk>', DetailBookView.as_view(), name='book'),
    path('create-book/', CreateBookView.as_view(), name='create_book'),
    path('users/', UserView.as_view(),name='users'),
    path("user/<int:pk>/", UserDetailView.as_view(), name="detail_user"),
    path("user/create/", CreateUserView.as_view(), name="create_user"),
    path('userbooks/', UserBookView.as_view(), name='userbooks'),
    path('userbook/<int:pk>/', DetailUserBookView.as_view(), name='userbook'),
    path('userbooks/create/', CreateUserBookView.as_view(), name='create_userbook'),
]

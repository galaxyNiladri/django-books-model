from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('book/<slug:slug>/', views.BookDetailsView.as_view(), name='book_info')
]
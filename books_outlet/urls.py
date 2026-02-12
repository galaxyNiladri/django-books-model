from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('book/<slug:slug>/', views.book_details, name='book_info')
]
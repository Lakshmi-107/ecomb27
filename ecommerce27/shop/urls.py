from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    # path('demo/',views.demo,name="demo"),
    path('', views.books, name="books"),
]

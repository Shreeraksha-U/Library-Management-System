from django.shortcuts import render, redirect
from .models import Book, Member, Borrow

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

from django.shortcuts import render

def index(request):
    return render(request, 'hobby_app/index.html')

def about(request):
    return render(request, 'hobby_app/about.html')

def contacts(request):
    return render(request, 'hobby_app/contacts.html')


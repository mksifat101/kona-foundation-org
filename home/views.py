from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def program(request):
    return render(request, 'home/program.html')


def event(request):
    return render(request, 'home/event.html')


def blog(request):
    return render(request, 'home/blog.html')


def contact(request):
    return render(request, 'home/contact.html')
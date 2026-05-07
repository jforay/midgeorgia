from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def equipment(request):
    return render(request, 'home/equipment.html')

def first_responders(request):
    return render(request, 'home/first_responders.html')

def dirty_work(request):
    return render(request, 'home/dirty_work.html')

def get_back(request):
    return render(request, 'home/get_back.html')
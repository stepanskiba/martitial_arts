from django.shortcuts import render, redirect


#
#
def index(request):
    return render(request, 'index.html')


def price(request):
    return render(request, 'price.html')


def instructor(request):
    return render(request, 'instructor.html')


def timetable(request):
    return render(request, 'timetable.html')

from django.shortcuts import render, redirect
from .models import PriceModels


#
#
def index(request):
    return render(request, 'index.html')


def price(request):
    object = PriceModels.objects.all()
    print(object)
    context = []
    for i in range(len(object)):
        context.append(object.values('description', 'number_of_trainings', 'cost')[i])

    return render(request, 'price.html', {'context': context})


def instructor(request):
    return render(request, 'instructor.html')


def timetable(request):
    return render(request, 'timetable.html')

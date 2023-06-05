from django.shortcuts import render, redirect
from .models import PriceModels, InstructorModels, UserModels

#
#
from django.shortcuts import render, redirect
from .models import UserModels


def index(request):
    if request.method == 'POST':
        surname = request.POST.get('last_name')
        name = request.POST.get('first_name')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        print(surname, name, phone, email)
        if surname and name and phone and email:
            UserModels.objects.create(surname=surname, name=name, phone=phone, email=email)
            return redirect('website:index')
        else:
            return redirect('website:index')
    return render(request, 'index.html')


def price(request):
    object = PriceModels.objects.all()
    print(object)
    context = []
    for i in range(len(object)):
        context.append(object.values('description', 'number_of_trainings', 'cost')[i])

    return render(request, 'price.html', {'context': context})


def instructor(request):
    object = InstructorModels.objects.all()
    print(object)
    context = []
    for i in range(len(object)):
        context.append(object.values('FIO', 'surname')[i])

    return render(request, 'instructor.html', {'context': context})


def timetable(request):
    return render(request, 'timetable.html')

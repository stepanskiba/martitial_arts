from .models import PriceModels, InstructorModels, UserModels, ReviewModels
from .models import TimetableModels, InformationOfInstructorModels

from django.shortcuts import render, redirect


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
    instructors = InstructorModels.objects.all()
    context = []

    for instructor in instructors:
        information = InformationOfInstructorModels.objects.filter(instructor__surname=instructor.surname)
        grouped_info = {}

        for info in information:
            if info.type not in grouped_info:
                grouped_info[info.type] = []
            grouped_info[info.type].append(info.information)

        if 'Направления' in grouped_info:
            directions = grouped_info.pop('Направления')
            grouped_info = {'Направления': directions, **grouped_info}

        context.append({
            'instructor': instructor,
            'information': grouped_info
        })

    return render(request, 'instructor.html', {'context': context})

# def instructor(request):
#     instructors = InstructorModels.objects.all()
#     context = []
#
#     for instructor in instructors:
#         information = InformationOfInstructorModels.objects.filter(instructor__surname=instructor.surname)
#         grouped_info = {}
#
#         for info in information:
#             if info.type not in grouped_info:
#                 grouped_info[info.type] = []
#             grouped_info[info.type].append(info.information)
#
#         context.append({
#             'instructor': instructor,
#             'information': grouped_info
#         })
#
#     return render(request, 'instructor.html', {'context': context})


def timetable(request):
    timetable_data = []

    # Получаем все объекты TimetableModels из базы данных
    timetables = TimetableModels.objects.all()

    # Создаем словарь, который будет хранить данные расписания для каждого временного слота
    schedule_data = {}

    # Заполняем словарь schedule_data данными из модели TimetableModels
    for timetable in timetables:
        time_slot = timetable.time_slot
        day = timetable.day
        instructor = timetable.instructor
        direction = timetable.direction

        if time_slot not in schedule_data:
            schedule_data[time_slot] = {}

        schedule_data[time_slot][day] = {'instructor': instructor, 'direction': direction}

    # Получаем список временных слотов, отсортированных по времени
    time_slots = sorted(schedule_data.keys())

    # Получаем список дней недели
    days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    # Создаем список словарей timetable_data для отображения в шаблоне
    for time_slot in time_slots:
        row_data = {'time_slot': time_slot}

        for day in days_of_week:
            instructor = schedule_data.get(time_slot, {}).get(day)
            row_data[day.lower() + '_instructor'] = instructor

        timetable_data.append(row_data)
    print(timetable_data)
    context = {'timetable_data': timetable_data}
    return render(request, 'timetable.html', context)


def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')
        print(name, review)
        if name and review:
            ReviewModels.objects.create(name=name, review=review)
            return redirect('website:review')
        else:
            return redirect('website:review')
    return render(request, 'review.html')

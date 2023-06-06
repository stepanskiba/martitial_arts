from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import CreateAbcForm
from .models import AlgoTask
from math import pi


def main(request):
    # print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            # print("\nform_is_valid:\n", form)
            form.save()
            return redirect('algo_task:form_result')
    else:
        form = CreateAbcForm()
        # print('\nform_else:\n', form)
    context = {'form': form}
    #  print("\ncontext:\n", context)
    return render(request, 'main.html', context)

def form_result(request):
    object = AlgoTask.objects.all().order_by('-id')[:1]
    print("object: ", object)
    # dict
    row = object.values('A', 'H', 'R', 'M')[0]
    print("row: ", row)
    # list
    row_list = object.values_list()[0]
    print("row_list: ", row_list)
    if row['A'] ** 3 >= row['M']:
        result_1 = "Поместиться в 1 емкость"
    else:
        result_1 = "Не поместиться в 1 емкость"

    if row['R'] ** 2 * pi * row['H'] >= row['M']:
        result_2 = "поместиться во 2 емкость"
    else:
        result_2 = "не поместиться во 2 емкость"
    # context
    result = result_1 + ', ' + result_2
    task = row_list[1]
    print('task: ', task)
    last_data = [row_list[2], row_list[3], row_list[4]]
    print('last_data:', last_data)
    print('result: ', result)
    context = {'task': task, 'last_data': last_data, 'result': result, 'row': row}
    return render(request, 'form_result.html', context)


def table(request):
    row = AlgoTask.objects.values()
    print('row:', row)
    row_lists = AlgoTask.objects.values_list()
    print('row_lists:', row_lists)
    cur_objects = AlgoTask.objects.all()
    statics_val = [cur_objects.aggregate(Count('M')), cur_objects.aggregate(Avg('M')), cur_objects.aggregate(Min('M')),
                   cur_objects.aggregate(Max('M')), cur_objects.aggregate(StdDev('M')), cur_objects.aggregate(Sum('M'))]
    print(statics_val)
    statics = {'statics_val': statics_val}

    fields = AlgoTask._meta.get_fields()
    print(fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print(verbose_name_list)
    print(name_list)
    field_names = verbose_name_list
    context = {'row': row, 'row_lists': row_lists, 'field_names': field_names, 'statics': statics}
    return render(request, 'table.html', context)

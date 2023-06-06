from django.urls import path

from . import views

app_name = 'algo_task'
urlpatterns = [
    path('', views.main, name='main'),
#    path('form_create_0/', views.form_create_0, name='form_create_0'),
    path('form_result/', views.form_result, name='form_result'),
    path('table/', views.table, name='table'),
]

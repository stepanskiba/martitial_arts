from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('price/', views.price, name='price'),
    path('instructor/', views.instructor, name='instructor'),
    path('timetable/', views.timetable, name='timetable'),
    path('review/', views.review, name='review')
]

#super commit
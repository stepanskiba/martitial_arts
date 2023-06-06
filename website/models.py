from django.db import models


# Create your models here.
class PriceModels(models.Model):
    description = models.CharField(max_length=225)
    number_of_trainings = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.id}&{self.description}"

    class Meta:
        verbose_name = "price"
        verbose_name_plural = "prices"
        ordering = ('number_of_trainings', 'cost')


class InstructorModels(models.Model):
    FIO = models.CharField(max_length=225)
    surname = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return f"{self.id}&{self.FIO}"

    class Meta:
        verbose_name = "instructor"
        verbose_name_plural = "instructors"
        ordering = ('id',)


class UserModels(models.Model):
    surname = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=225)
    current_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}&{self.surname}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ('id',)


class ReviewModels(models.Model):
    name = models.CharField(max_length=200)
    review = models.CharField(max_length=5000)
    current_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}&{self.name}"

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        ordering = ('id',)


class TimetableModels(models.Model):
    instructor = models.ForeignKey(InstructorModels, on_delete=models.CASCADE, to_field='surname',
                                   db_column='instructor_surname')
    day = models.CharField(max_length=5)
    time_slot = models.CharField(max_length=15)
    direction = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}&{self.instructor_id}"

    class Meta:
        verbose_name = "timetable"
        verbose_name_plural = "timetable"
        ordering = ('time_slot',)


class InformationOfInstructorModels(models.Model):
    instructor = models.ForeignKey(InstructorModels, on_delete=models.CASCADE, to_field='surname',
                                   db_column='instructor_surname')
    type = models.CharField(max_length=225)
    information = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id}&{self.instructor}"

    class Meta:
        verbose_name = "information of instructor"
        verbose_name_plural = "information of instructors"
        ordering = ('id',)

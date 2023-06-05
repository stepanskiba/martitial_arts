from django.db import models


# Create your models here.
class PriceModels(models.Model):
    description = models.CharField('sasa', max_length=225)
    number_of_trainings = models.IntegerField('s')
    cost = models.IntegerField('sa')

    def __str__(self):
        return f"{self.id}&{self.description}"

    class Meta:
        verbose_name = "price"
        verbose_name_plural = "prices"
        ordering = ('number_of_trainings', 'cost')


class InstructorModels(models.Model):
    FIO = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)

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

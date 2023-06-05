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


a = PriceModels('Пробное занятие', '1', '300')
print(a)
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

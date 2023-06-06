from django.db import models


class AlgoTask(models.Model):
    task = models.CharField("Формулировка задачи",
                            default="1007. Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.",
                            max_length=255)
    A = models.IntegerField("Ребро куба", default=0, )
    H = models.IntegerField("Высота цилиндра", default=0, )
    R = models.IntegerField("Радиус цилиндра", default=0, )
    M = models.IntegerField("Обьем жидкости", default=0)
    current_date = models.DateTimeField("Дата изменения(save)", auto_now=True)

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"{self.id}&{self.task}"

    class Meta:
        verbose_name = "A_H_R_M"
        verbose_name_plural = "A_H_R_M_S"
        ordering = ('-id', '-M')

# python manage.py makemigrations
# python manage.py migrate

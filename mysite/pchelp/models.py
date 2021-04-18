from django.db import models


class Feedback(models.Model):
    first_name = models.CharField(max_length=200, verbose_name = 'Ваше имя:')
    email = models.CharField(max_length=200, verbose_name = 'Номер телефона или почта:')
    item = models.CharField(max_length=100, verbose_name = 'С чем имеем дело?')
    problem = models.CharField(max_length=500, verbose_name = 'Опишите в кратце вашу проблему:')

    def __str__(self):
        return self.item + '_' + self.first_name



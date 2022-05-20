from django.db import models


# Create your models here.
class Rated(models.Model):
    name = models.CharField('名稱', max_length=5, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分級'
        verbose_name_plural = '分級'


class Director(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)
    gender = models.BooleanField('性別', choices=((True, '男'), (False, '女')))
    birth = models.DateTimeField('生日')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '導演'
        verbose_name_plural = '導演'


class Type(models.Model):
    name = models.CharField('名稱', max_length=5, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '類型'
        verbose_name_plural = '類型'


class Movie(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)
    content = models.TextField('介紹', max_length=350)
    rated = models.ForeignKey(Rated, on_delete=models.PROTECT, verbose_name='分級')
    director = models.ForeignKey(Director, on_delete=models.PROTECT, verbose_name='導演')
    playdate = models.DateTimeField('上映日')

    types = models.ManyToManyField(Type, verbose_name='類型')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '電影'
        verbose_name_plural = '電影'


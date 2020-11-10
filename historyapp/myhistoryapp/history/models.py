from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Personality(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField('Картинка', upload_to='static/img', height_field=None, width_field=None, max_length=100,
null=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Личности'
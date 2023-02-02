from django.db import models

class Info_index(models.Model):
    title = models.CharField('Название', max_length=100)
    content = models.TextField('Содержимое', blank=True) #текстовое поле

    class Meta:  # используем вспомогательный класс мета для сортировки наших дел
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return self.title
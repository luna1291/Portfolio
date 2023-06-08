from django.db import models


class Projects(models.Model):
    title = models.CharField('Название', max_length=100)
    short_disc = models.TextField('Краткое описание')
    text = models.TextField('Описание проекта')
    attach = models.FileField('Ссылка', default="", null=True, blank=True)
    photo_link = models.ImageField('Фото', default="", upload_to='img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

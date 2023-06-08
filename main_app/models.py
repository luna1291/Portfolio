from django.db import models


class HomePage(models.Model):
    quote = models.TextField('Цитата')
    text = models.TextField('Приветствие')
    photo = models.ImageField('Фото', default="", upload_to='img/', blank=True)
    
    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Приветствие'
        verbose_name_plural = 'Приветствия'

class AboutPage(models.Model):
    id = models.CharField(primary_key=True, serialize=False, max_length=100)
    about_shert = models.CharField('Название', max_length=250)
    header = models.CharField('Заголовок', max_length=250, null=True)
    topbox = models.TextField('Опыт')
    header2 = models.CharField('Заголовок', max_length=250, null=True)
    botbox= models.TextField('Навыки')
    image = models.ImageField('Шкала', default="", upload_to='img/', blank=True)
    
    def __str__(self):
        return self.about_shert

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессия'
    
class Serts(models.Model):
    id = models.IntegerField(primary_key=True)
    sert_name = models.CharField('Название', max_length=250)
    serts = models.ImageField('Сертификаты', default="", upload_to='img/')
    
    def __str__(self):
        return self.sert_name

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
    
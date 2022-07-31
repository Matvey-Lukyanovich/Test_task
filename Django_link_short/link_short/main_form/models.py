from django.db import models


class Shortcut_link(models.Model):
    user_info = models.CharField('Пользователь', max_length=51)
    link_info = models.CharField('Начальная ссылка', max_length=51)
    link_short = models.CharField('Конечная ссылка', max_length=51)

    def __str__(self):
        return self.user_info

    class Meta:
        verbose_name = "Элемент ссылки"
        verbose_name_plural = "Сокращенные ссылки:"
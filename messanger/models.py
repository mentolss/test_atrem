from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class FeedbackUser(models.Model):
    class StatusChoices(models.TextChoices):
        COMPLETE = 'Решено'
        WAITING = 'Ожидает'
        UNRESOLVED = 'Нет решения'

    name = models.CharField(max_length=100, verbose_name=u"Имя")
    phone_number = models.CharField(max_length=20, verbose_name=u"Номер телефона")
    message = models.TextField(verbose_name=u"Проблема")
    timestamp = models.DateTimeField(verbose_name=u"Дата заявки")
    status = models.CharField(choices=StatusChoices.choices, max_length=16, default=StatusChoices.WAITING,
                              verbose_name=u"Статус ответа на заявку")

    class Meta:
        verbose_name = 'Заявка обратной связи'
        verbose_name_plural = 'Заявки обратной связи'

    def save(self, *args, **kwargs):
        if self.timestamp and self.timestamp.tzinfo is None:
            now = datetime.now()
            belarus_offset = timedelta(hours=2) if now.month >= 4 and now.month <= 10 else timedelta(hours=3)
            self.timestamp += belarus_offset
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

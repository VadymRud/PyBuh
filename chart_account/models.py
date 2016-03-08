#chart_account
from django.db import models
import uuid
from datetime import datetime

class BaseChartAccaunt(models.Model):
    code = models.UUIDField( default=uuid.uuid4, verbose_name = 'Unique code')
    date = models.DateTimeField(default=datetime.now, verbose_name = 'Дата Создания')
    active = models.BooleanField(verbose_name = 'Активный', default=True)
    name = models.CharField(max_length=255, verbose_name = 'Полное имя')
    number = models.CharField(max_length=255, verbose_name = 'Полное имя')
    class Meta:
       abstract = True


class Through(BaseChartAccaunt):
    pass
    #some = models.CharField(max_length=100, verbose_name = 'Полное имя')

class ChartAccaunt(BaseChartAccaunt):
    through = models.ForeignKey(Through, related_name='through___qqq')
    
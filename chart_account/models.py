#chart_account
from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class BaseChartAccaunt(models.Model):
    code = models.UUIDField( default=uuid.uuid4, verbose_name = _('Unique code'))
    date = models.DateTimeField(default=datetime.now, verbose_name = _('Date creation'))
    active = models.BooleanField(verbose_name = _('Active'), default=True)
    name = models.CharField(max_length=255, verbose_name = _('Full name'))
    number = models.CharField(max_length=255, verbose_name = _('Number'))
    class Meta:
       abstract = True


class Through(BaseChartAccaunt):
    pass
    #some = models.CharField(max_length=100, verbose_name = 'Полное имя')

class ChartAccaunt(BaseChartAccaunt):
    through = models.ForeignKey(Through, related_name='through', verbose_name = _('Through'))
    
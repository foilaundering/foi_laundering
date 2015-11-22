from datetime import timedelta, datetime
from random import randrange

from django.db import models

def random_date_in_future():
    min_in_future = 14 # 2 weeks
    max_in_future = 70 # 10 weeks
    delta = randrange(min_in_future, max_in_future)
    return datetime.now() + timedelta(days=delta)

class Authority(models.Model):
    name = models.CharField(blank=True, max_length=255)
    slug = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name


class FOIRequest(models.Model):
    title = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="A one line summary of the information you are requesting, \
        e.g. 'Crime statistics by ward level for Wales'")
    foi_text = models.TextField(blank=False, verbose_name="Your FOI Request")
    make_live_date = models.DateTimeField(
        blank=False, default=random_date_in_future)
    sent = models.BooleanField(default=False)
    receiving_authority = models.ForeignKey(Authority)

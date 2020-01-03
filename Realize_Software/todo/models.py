from django.db import models


class Todo(models.Model):
    name = models.CharField('NAME', max_length=10, blank=True)
    dtime = models.CharField('DTIME', max_length=10)
    todo = models.CharField('TODO', max_length=100)

from django.db import models

from django.contrib.auth.models import User



class Seminar(models.Model):
    class Meta:
        verbose_name_plural = 'Seminar'

    title = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    conducted = models.CharField(max_length=200, null=False, blank=False)
    date_started = models.CharField(max_length=200, null=False, blank=False)
    date_ended = models.CharField(max_length=200, null=False, blank=False)
    time_duration = models.CharField(max_length=200, null=False, blank=False)
    seminar_type = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.title
        return name


class Workshop(models.Model):
    class Meta:
        verbose_name_plural = 'Workshop'

    title = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    conducted = models.CharField(max_length=200, null=False, blank=False)
    date_started = models.CharField(max_length=200, null=False, blank=False)
    date_ended = models.CharField(max_length=200, null=False, blank=False)
    time_duration = models.CharField(max_length=200, null=False, blank=False)
    seminar_type = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.title
        return name

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skill'

    title = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    conducted = models.CharField(max_length=200, null=False, blank=False)
    date_started = models.CharField(max_length=200, null=False, blank=False)
    date_ended = models.CharField(max_length=200, null=False, blank=False)
    time_duration = models.CharField(max_length=200, null=False, blank=False)
    skill_type = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.title
        return name

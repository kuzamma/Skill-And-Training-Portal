import django_filters
from .models import *

class SeminarFilter(django_filters.FilterSet):
    class Meta:
        model = Seminar
        fields = ['title']

class WorkshopFilter(django_filters.FilterSet):
    class Meta:
        model = Workshop
        fields = ['title']

class SkillFilter(django_filters.FilterSet):
    class Meta:
        model = Skill
        fields = ['title']


import django_filters
from .models import *


class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Account
        fields = ('id', 'username')


class MeetApplFilter(django_filters.FilterSet):

    class Meta:
        model = ApplicationMet
        fields = ('id', 'meeting')


class GroupFilter(django_filters.FilterSet):

    class Meta:
        model = Group
        fields = '__all__'
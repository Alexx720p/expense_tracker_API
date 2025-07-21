import django_filters
from django.utils import timezone
from datetime import datetime, time, timedelta
from .models import Expense
from django_filters import rest_framework as filters

class ExpenseFilter(django_filters.FilterSet):
    date_preset = django_filters.CharFilter(method='filter_by_preset')
    date = django_filters.DateFilter(method='filter_by_day')


    class Meta:
        model = Expense
        fields = ['date_preset', 'date', 'title', 'category']

    def filter_by_preset(self, queryset, name, value):
        now = timezone.now()

        presets = {
        'past_week': now - timedelta(days=7),
        'past_month': now - timedelta(days=30),
        'past_3_months': now - timedelta(days=90),
    }

        start = presets.get(value)
        if start:
            return queryset.filter(date__range=(start, now))
        return queryset

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        start = self.data.get('start_date')
        end = self.data.get('end_date')

        if start:
            start_dt = timezone.make_aware(datetime.combine(
                datetime.strptime(start, '%Y-%m-%d'), time.min))
            queryset = queryset.filter(date__gte=start_dt)

        if end:
            end_dt = timezone.make_aware(datetime.combine(
                datetime.strptime(end, '%Y-%m-%d'), time.max))
            queryset = queryset.filter(date__lte=end_dt)

        return queryset

    def filter_by_day(self, queryset, name, value):
        start = timezone.make_aware(datetime.combine(value, time.min))
        end = timezone.make_aware(datetime.combine(value, time.max))
        return queryset.filter(date__range=(start, end))

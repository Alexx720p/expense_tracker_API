from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Leisure', 'Leisure'),
        ('Electronics', 'Electronics'),
        ('Utilities', 'Utilities'),
        ('Clothing', 'Clothing'),
        ('Health', 'Health'),
        ('Others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.date and timezone.is_naive(self.date):
            self.date = timezone.make_aware(self.date)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
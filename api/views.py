from rest_framework import viewsets, filters
from .models import Expense
from .serializer import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .filters import ExpenseFilter
from django_filters.rest_framework import DjangoFilterBackend

class ExpenseView(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter

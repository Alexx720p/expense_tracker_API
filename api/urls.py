from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseView

router = DefaultRouter()
router.register(r'expenses', ExpenseView)

urlpatterns = [
    path('', include(router.urls)),
]
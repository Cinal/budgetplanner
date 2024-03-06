from django.urls import path

from .views import (
    BudgetDetailView,
    BudgetListView,
    SharedBudgetDetailView,
    SharedBudgetListView,
    TransactionDetailView,
    TransactionListView,
)

urlpatterns = [
    path("budgets/", BudgetListView.as_view(), name="budget-list"),
    path("budgets/<int:pk>/", BudgetDetailView.as_view(), name="budget-detail"),
    path("transactions/", TransactionListView.as_view(), name="transaction-list"),
    path("transactions/<int:pk>/", TransactionDetailView.as_view(), name="transaction-detail"),
    path("shared-budgets/", SharedBudgetListView.as_view(), name="shared-budget-list"),
    path("shared-budgets/<int:pk>/", SharedBudgetDetailView.as_view(), name="shared-budget-detail"),
]

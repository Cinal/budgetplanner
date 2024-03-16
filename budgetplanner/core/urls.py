from core.views import (
    BudgetDetailView,
    BudgetListView,
    ShareBudgetView,
    SharedBudgetDetailView,
    SharedBudgetListView,
    TransactionDetailView,
    TransactionListView,
    UnshareBudgetView,
)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.views import (
    RegisterApi,
)

urlpatterns = [
    path("register/", RegisterApi.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("budgets/", BudgetListView.as_view(), name="budget-list"),
    path("budgets/<int:pk>/", BudgetDetailView.as_view(), name="budget-detail"),
    path("budgets/<int:budget_id>/share/", ShareBudgetView.as_view(), name="budget-share"),
    path("budgets/<int:budget_id>/unshare/", UnshareBudgetView.as_view(), name="budget-unshare"),
    path("transactions/", TransactionListView.as_view(), name="transaction-list"),
    path("transactions/<int:pk>/", TransactionDetailView.as_view(), name="transaction-detail"),
    path("shared-budgets/", SharedBudgetListView.as_view(), name="shared-budget-list"),
    path("shared-budgets/<int:pk>/", SharedBudgetDetailView.as_view(), name="shared-budget-detail"),
]
